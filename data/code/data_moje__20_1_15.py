def is_even(number):
    return (number & 1) == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 10, 101, 100, 999]
    for value in sample_values:
        print(is_even(value))