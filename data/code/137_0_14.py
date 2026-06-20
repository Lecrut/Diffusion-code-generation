def check_even_odd(number):
    return number & 1 == 0

if __name__ == '__main__':
    sample_values = [2, 3, 4, 5, 6, -8, -7]
    for value in sample_values:
        result = check_even_odd(value)
        print(f'Number: {value}, Is Even: {result}')