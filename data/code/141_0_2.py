def logical_and(a, b):
    return a & b

def logical_or(a, b):
    return a | b

def logical_not(a):
    return ~a + 2
if __name__ == '__main__':
    print(logical_and(True, True))
    print(logical_or(False, True))
    print(logical_not(True))