def is_even(number: int) -> bool:
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [4, 7, -2, 0, 15]
    for val in test_values:
        result = is_even(val)
        print(f"{val}: {result}")