def is_even(number):
    return (number & 1) == 0

if __name__ == '__main__':
    sample_values = [4, 7, 0, -2, 15]
    for val in sample_values:
        print(is_even(val))