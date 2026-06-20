def is_odd(num):
    if not isinstance(num, int):
        raise ValueError('Input must be an integer')
    return num & 1 == 1
if __name__ == '__main__':
    print(is_odd(3))
    print(is_odd(4))