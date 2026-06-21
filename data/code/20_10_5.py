def is_even(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError("Input must be an integer")
    return (value & 1) == 0

if __name__ == '__main__':
    test_values = [4, 7, 0, -3]
    for n in test_values:
        result = is_even(n)
        print(result)