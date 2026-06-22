METERS_PER_KILOMETER = 1000

def convert_kilometers_to_meters(value_km: int) -> int:
    if not isinstance(value_km, int) or isinstance(value_km, bool):
        raise TypeError("Input must be a non-boolean integer")
    return value_km * METERS_PER_KILOMETER

if __name__ == '__main__':
    test_cases = [1, 12, 0, -50]
    for km_val in test_cases:
        meters = convert_kilometers_to_meters(km_val)
        print(meters)