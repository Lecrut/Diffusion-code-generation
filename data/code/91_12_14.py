from functools import reduce
from operator import xor

NEGATE_MAP = {True: False, False: True}

def negate(val):
    if val not in NEGATE_MAP:
        raise ValueError("Input must be a boolean")
    return reduce(xor, (val, True))

if __name__ == '__main__':
    print(negate(True))
    print(negate(False))