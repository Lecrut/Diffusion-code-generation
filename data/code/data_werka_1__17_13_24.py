def is_even(number):
    return number & 1 == 0
if __name__ == '__main__':
    print(is_even(2))
    print(is_even(-4))
    print(is_even(3))
    print(is_even(0))
    print(is_even(7))