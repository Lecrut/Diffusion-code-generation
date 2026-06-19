def is_odd(number):
    return number & 1 != 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, 16, 31, 64]
    for value in sample_values:
        print(f"{value} is odd: {is_odd(value)}")