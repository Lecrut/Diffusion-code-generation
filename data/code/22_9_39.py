def is_odd(num):
    return bool(num & 1)
if __name__ == '__main__':
    print(is_odd(3))
    print(is_odd(4))
    print(is_odd(-5))
    print(is_odd(0))