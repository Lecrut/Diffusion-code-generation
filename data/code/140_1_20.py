def is_even(number):
    return number & 1 == 0

if __name__ == '__main__':
    sample_value = 42
    print(is_even(sample_value))