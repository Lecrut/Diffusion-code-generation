def decimal_to_binary(number: int) -> str:
    if number < 0:
        raise ValueError("Input must be a positive decimal integer")
    return f"{number:b}"

if __name__ == '__main__':
    test_values = [0, 1, 2, 5, 10, 255, 1024, 65535]
    for value in test_values:
        print(decimal_to_binary(value))