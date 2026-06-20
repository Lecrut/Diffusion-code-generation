def is_number_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    sample_values = [-5, -3, 0, 1, 4, 7]
    for value in sample_values:
        print(f"{value}: {is_number_odd(value)}")