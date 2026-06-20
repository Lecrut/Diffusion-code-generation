IS_ODD_BIT_MASK = 1

def is_odd(n):
    return n & IS_ODD_BIT_MASK != 0
if __name__ == '__main__':
    print(is_odd(4))
    print(is_odd(5))