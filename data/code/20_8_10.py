def is_even(number: int) -> bool:
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [-4, -3, 0, 2, 7, 10]
    for value in test_values:
        result = is_even(value)
        print(f"{value}: {result}")