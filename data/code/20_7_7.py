def _validate_integer(value: int) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)

def is_even(value: int) -> bool:
    if not _validate_integer(value):
        return False
    return value % 2 == 0

if __name__ == '__main__':
    test_values = [10, 17, -4, 0, 1001, 23456]
    for num in test_values:
        print(is_even(num))