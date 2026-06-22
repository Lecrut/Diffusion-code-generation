def is_divisible_by_two(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [10, 15, 32, -4, 0, 1]
    for value in test_values:
        print(is_divisible_by_two(value))