#!/usr/bin/env python3
'''creating a unique file storage instance for our application.'''
from engine.file_storage import FileStorage

storage = FileStorage()
reload(storage)
