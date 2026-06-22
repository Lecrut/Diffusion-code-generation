def is_even(number: int) -> bool:
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 100, -5, 0]
    for val in test_values:
        result = is_even(val)
        print(result)