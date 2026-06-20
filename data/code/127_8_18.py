def is_odd(number):
    return number & 1 != 0
if __name__ == '__main__':
    print(is_odd(3))
    print(is_odd(4))
    print(is_odd(-1))
    print(is_odd(-2))