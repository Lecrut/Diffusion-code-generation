def is_divisible_by_two(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [4, 7, 10, -2, -5, 0]
    for value in test_values:
        print(is_divisible_by_two(value))