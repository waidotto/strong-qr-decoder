#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'sqrd - Strong QR Decoder')
	parser.add_argument('-v', '--verbose', action = 'store_true', help = 'show detailed information')
	parser.add_argument('FILE', nargs = '?', default = '-', help = 'QR text file (default is -, standard input)')
	args = parser.parse_args()
	print args
