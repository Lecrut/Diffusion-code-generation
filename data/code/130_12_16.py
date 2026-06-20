def is_zero(value: int) -> bool:
    return value == 0

if __name__ == '__main__':
    test_values = [0, 5, -10, 0, 3.14]
    for val in test_values:
        result = is_zero(val)
        print(f"Checking value: {val}, Result: {result}")