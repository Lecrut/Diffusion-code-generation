KILMETERS_TO_METERS_FACTOR = 1000

def validate_distance(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    if value < 0:
        raise ValueError("Input must be non-negative")

def to_meters(kilometers):
    validate_distance(kilometers)
    return kilometers * KILMETERS_TO_METERS_FACTOR

if __name__ == '__main__':
    test_cases = [0, 5, 12.5, -1, "invalid"]
    for case in test_cases:
        try:
            print(to_meters(case))
        except (ValueError, TypeError) as error:
            print(error)