def is_even(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return (number & 1) == 0

if __name__ == '__main__':
    test_values = [4, 7, 0, -3, 100]
    for val in test_values:
        print(is_even(val))