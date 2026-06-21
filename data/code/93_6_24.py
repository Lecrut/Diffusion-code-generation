from operator import xor
from functools import reduce
from operator import and_

CHECK_FALSE = False
CHECK_TRUE = True

def check_both_false(a, b):
    bools = [bool(a), bool(b)]
    true_count = reduce(and_, bools, CHECK_TRUE)
    return xor(true_count, CHECK_TRUE)

if __name__ == '__main__':
    a = 0
    b = []
    result = check_both_false(a, b)
    print(result)