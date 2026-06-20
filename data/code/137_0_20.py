def check_even_odd(number):
    return number & 1 == 0
if __name__ == '__main__':
    sample_values = [4, 7, 23, 42]
    for value in sample_values:
        result = check_even_odd(value)
        print(f'Input: {value}, Is Even: {result}')