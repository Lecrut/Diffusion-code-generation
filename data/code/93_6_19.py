TRUE_VALUE = 1
FALSE_VALUE = 0
ZERO = 0

def are_both_false(a, b):
    return int(not a) == FALSE_VALUE and int(not b) == FALSE_VALUE

if __name__ == '__main__':
    a = 0
    b = None
    result = are_both_false(a, b)
    print(result)