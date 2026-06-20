IS_ODD_MASK = 1

def is_odd(n):
    return n & IS_ODD_MASK != 0
if __name__ == '__main__':
    print(is_odd(3))
    print(is_odd(4))