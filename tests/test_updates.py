#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# This file is part of command_runner module

"""
Get updates installed by Windows Update, including those the QFE doesn't list

Versioning semantics:
    Major version: backward compatibility breaking changes
    Minor version: New functionality
    Patch version: Backwards compatible bug fixes

"""

__intname__ = 'tests.windows_tools.updates'
__author__ = 'Orsiris de Jong'
__copyright__ = 'Copyright (C) 2021 Orsiris de Jong'
__licence__ = 'BSD 3 Clause'
__build__ = '2021100501'


from windows_tools.updates import *


def test_get_windows_updates_reg():
    updates = get_windows_updates_reg()
    assert isinstance(updates, list), 'Result should be a list'


def test_get_windows_updates_wmi():
    updates = get_windows_updates_wmi()
    assert isinstance(updates, list), 'Result should be a list'


def test_get_windows_updates_com():
    updates = get_windows_updates_com()
    assert isinstance(updates, list), 'Result should be a list'


def test_get_all_windows_updates():
    updates = get_windows_updates()

    assert isinstance(updates, list), 'Result should be a list'

    for update in updates:
        print(update)


def test_get_windows_updates_filtered():
    updates = get_windows_updates(filter_duplicates=True)

    assert isinstance(updates, list), 'Result should be a list'

    already_seen_titles = []
    already_seen_kb = []
    for update in updates:
        if update['title'] not in already_seen_titles:
            already_seen_titles.append(update['title'])
        elif update['title'] and update['title'] in already_seen_titles:
            print(update)
            assert False, 'We have a title double'
        if update['kb'] not in already_seen_kb:
            already_seen_kb.append(update['kb'])
        elif update['kb'] and update['kb'] in already_seen_kb:
            print(update)
            assert False, 'We have a double KB'



if __name__ == '__main__':
    print('Example code for %s, %s' % (__intname__, __build__))
    test_get_windows_updates_reg()
    test_get_windows_updates_wmi()
    test_get_windows_updates_com()
    test_get_all_windows_updates()
    test_get_windows_updates_filtered()