def is_even(number):
    return (number & 1) == 0

if __name__ == '__main__':
    sample_values = [4, 7, 8, -2, -5]
    for value in sample_values:
        print(f"{value}: {is_even(value)}")