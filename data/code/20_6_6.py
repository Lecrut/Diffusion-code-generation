def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 100, 101, -2, -3, 7]
    for value in test_values:
        result = is_even(value)
        print(f"{value}: {result}")