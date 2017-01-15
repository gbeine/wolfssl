# -*- coding: utf-8 -*-
#
# conftest.py
#
# Copyright (C) 2006-2016 wolfSSL Inc.
#
# This file is part of wolfSSL. (formerly known as CyaSSL)
#
# wolfSSL is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# wolfSSL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

# pylint: disable=missing-docstring, redefined-outer-name

import socket
import ssl
import wolfssl
import pytest

@pytest.fixture
def tcp_socket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        yield sock

@pytest.fixture(params=[ssl, wolfssl], ids=["ssl", "wolfssl"])
def ssl_provider(request):
    return request.param

@pytest.fixture
def ssl_context(ssl_provider):
    return ssl_provider.SSLContext(ssl_provider.PROTOCOL_SSLv23)
