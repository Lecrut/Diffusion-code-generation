def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [2, 3, 4, 7, 10]
    for value in sample_values:
        result = is_even(value)
        print(f"{value}: {result}")