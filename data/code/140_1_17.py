def is_even(number):
    if not isinstance(number, int):
        raise ValueError('Input must be an integer')
    return number & 1 == 0
if __name__ == '__main__':
    print(is_even(4))
    print(is_even(5))