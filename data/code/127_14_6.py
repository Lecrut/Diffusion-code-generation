def is_odd(n):
    return n & 1 == 1
if __name__ == '__main__':
    print(is_odd(3))
    print(is_odd(4))
    print(is_odd(-1))
    print(is_odd(0))