import time

from opc_ua_operations import *


class PackS:
    finished = 0
    fix_box_upper_side = 'ns=4;i=44'
    fix_box_tongue = 'ns=4;i=45'
    pack_box = 'ns=4;i=46'

    def __init__(self):
        print("PackS created")

    @classmethod
    def start(cls):
        write_value_bool(cls.fix_box_tongue, True)
        time.sleep(2)
        write_value_bool(cls.fix_box_upper_side, False)
        time.sleep(2)
        write_value_bool(cls.pack_box, True)
        time.sleep(2)
        write_value_bool(cls.pack_box, False)
        time.sleep(2)
        write_value_bool(cls.fix_box_tongue, False)
        time.sleep(2)

        cls.finished = 1
