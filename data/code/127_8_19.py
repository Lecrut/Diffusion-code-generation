def is_odd(number):
    return number & 1 != 0
if __name__ == '__main__':
    print(is_odd(5))
    print(is_odd(6))
    print(is_odd(-3))
    print(is_odd(-4))