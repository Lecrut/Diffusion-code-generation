def is_even(number):
    return not (number & 1)

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))