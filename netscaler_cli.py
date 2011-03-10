#!/usr/bin/python

# module netscaler_cli.py
#
# Jesse Davis (jesse.michael.davis@gmail.com)

"""
Common code for Netscaler CLI tools.
"""

import ConfigParser
import httplib2
import logging
from optparse import OptionParser
import os
import sys

def initializeOptions(usage=None):
    default_cfg = os.path.join(os.environ['HOME'],'.ns_tools.cfg')
    parser = OptionParser()

    parser.set_usage(usage)
    parser.set_defaults(verbose=False, quiet=False, credentials_file=default_cfg)
    parser.add_option("-f", "--creds_file", action="store", type="string", 
	              dest="credentials_file", help='Credentials file, default is $HOME/.ns_tools.cfg')
    parser.add_option("-v", dest="verbose", action="store_true",
	              help="Print extra logging info.")
    parser.add_option("-q", dest="quiet", action="store_true",
	              help="Print no logging info.")

    return parser

def initializeLog(logger_name='ns_cli_tools'):
    log = logging.getLogger(logger_name)
    log_level = logging.WARNING

    log.setLevel(log_level)
    handler = logging.StreamHandler()
    handler.setLevel(log_level)
    log_format = "%(asctime)s - %(levelname)s: %(message)s"
    handler.setFormatter(logging.Formatter(log_format))
    log.addHandler(handler)

    return log

def initializeConfigParser(filename):
    config = ConfigParser.ConfigParser()

    config.read(filename)
    config_section = 'creds'

    creds = {}
    creds['ws_url'] = config.get(config_section, 'ws_url')
    creds['username'] = config.get(config_section, 'username')
    creds['password'] = config.get(config_section, 'password')

    return creds
