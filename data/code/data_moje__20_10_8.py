def is_even(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return (number & 1) == 0

if __name__ == "__main__":
    test_values = [0, 1, 2, -4, 101, 256]
    for value in test_values:
        print(value, is_even(value))