def bit_and(a, b):
    return a & b

def bit_or(a, b):
    return a | b

def bit_not(a):
    return ~a
if __name__ == '__main__':
    print(bit_and(5, 3))
    print(bit_or(5, 3))
    print(bit_not(5))