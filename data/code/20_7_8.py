def is_even(value: int) -> bool:
    return value % 2 == 0

if __name__ == '__main__':
    test_values = [2, 3, 0, -4, 1001]
    for num in test_values:
        print(is_even(num))