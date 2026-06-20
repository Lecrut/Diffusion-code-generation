def bitmask_and(a, b):
    return a & b

def bitmask_or(a, b):
    return a | b

def bitmask_not(a):
    return ~a
if __name__ == '__main__':
    print(bitmask_and(12, 10))
    print(bitmask_or(12, 10))
    print(bitmask_not(12))