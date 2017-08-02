# -*- coding: utf-8 -*-

# needed for python 3 compatibility
from __future__ import unicode_literals, print_function, division, absolute_import

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from neo.rawio.winwcprawio import WinWcpRawIO
from neo.rawio.tests.common_rawio_test import BaseTestRawIO


class TestWinWcpRawIO(BaseTestRawIO, unittest.TestCase, ):
    rawioclass = WinWcpRawIO
    files_to_test = ['File_winwcp_1.wcp']
    files_to_download = files_to_test

if __name__ == "__main__":
    unittest.main()

