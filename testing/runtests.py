# -*- coding: utf-8 -*-

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    args = sys.argv
    args.insert(1, "test")
    args.insert(2, "pg_uuid_fields")

    execute_from_command_line(args)
