def is_number_odd(number):
    if not isinstance(number, int):
        raise ValueError('Input must be an integer')
    return number % 2 != 0
if __name__ == '__main__':
    print(f'1: {is_number_odd(1)}')
    print(f'-3: {is_number_odd(-3)}')
    print(f'4: {is_number_odd(4)}')
    print(f'-2: {is_number_odd(-2)}')