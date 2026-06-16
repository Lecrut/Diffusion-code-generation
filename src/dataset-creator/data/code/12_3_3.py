def is_strict_odd_integer(value: int) -> bool:
    return value % 2 != 0
if __name__ == '__main__':
    test_values = [1, -3, 4, 5, 0]
    for val in test_values:
        result = "Yes" if is_strict_odd_integer(val) else "No"
        print(f"{val}: {result}")