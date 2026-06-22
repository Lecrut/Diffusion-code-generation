CONVERSION_FACTOR = 1000

def _validate_kilometers(value: int) -> None:
    if not isinstance(value, int):
        raise TypeError("Input must be an integer")
    if value < 0:
        raise ValueError("Input must be non-negative")

def convert_kilometers_to_meters(km: int) -> int:
    _validate_kilometers(km)
    return km * CONVERSION_FACTOR

if __name__ == '__main__':
    test_cases = [42, 100, 0]
    for val in test_cases:
        result = convert_kilometers_to_meters(val)
        print(result)