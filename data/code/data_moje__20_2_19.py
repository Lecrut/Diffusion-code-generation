def is_even(number: int) -> bool:
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 17, 100, -4, -3]
    for value in test_values:
        result = is_even(value)
        print(f"{value}: {result}")