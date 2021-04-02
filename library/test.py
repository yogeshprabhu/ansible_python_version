#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import sys 


def main():
    module = AnsibleModule(argument_spec={})
    version = sys.version
    module.exit_json(changed=False,meta=version) 

if __name__ == '__main__': main()