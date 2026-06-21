def is_even(number):
    return number & 1 == 0

if __name__ == '__main__':
    sample_values = [2, 3, 0, -4, -5, 10, -11, 12]
    for value in sample_values:
        result = is_even(value)
        print(f"{value} is even: {result}")