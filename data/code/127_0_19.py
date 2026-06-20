ODD_CHECK_MASK = 1

def is_odd(n):
    return n & ODD_CHECK_MASK != 0

if __name__ == '__main__':
    print(is_odd(3))
    print(is_odd(4))