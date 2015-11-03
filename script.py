#!/usr/bin/env python
import os
for key in os.environ:
    print("%s=%s" % (key, os.environ[key]))
