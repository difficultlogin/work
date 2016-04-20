#!/usr/bin/env python3

import sys, os, subprocess

try:
	name = sys.argv[1]
except IndexError:
	print('sudo ./create_domain.py [domain_name]')
	exit()

template = open('/etc/apache2/sites-available/test.conf').read()
new_conf_uri = '/etc/apache2/sites-available/%s.conf' % name
document_root = '/home/ilnur/webserver/%s.bit' % name

if os.path.exists(new_conf_uri):
	print('ERROR: file %s.conf is exist')
	exit()

with open(new_conf_uri, 'w+') as new_conf:
	new_conf.write(template.replace('test', name))
	print('file %s.conf is created' % name)

if os.path.exists(document_root):
	print('directory %s is exist' % name)
else:
	os.mkdir(document_root)
	print('directory %s is created: %s' % (name, document_root))
	os.popen('chown -R ilnur:ilnur %s' % document_root)

print(os.popen('cd /etc/apache2/sites-available; a2ensite %s.conf' % name).read())
print(os.popen('service apache2 reload').read())

hosts = open('/etc/hosts', 'a')
hosts.write('127.0.0.1 %s.bit\n' % name)
print('add 127.0.0.1 %s.bit to /etc/hosts' % name)
