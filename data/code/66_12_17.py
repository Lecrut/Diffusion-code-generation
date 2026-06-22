METERS_PER_KILOMETER = 1000

def convert_km_to_m(kilometers):
    if not isinstance(kilometers, int):
        raise TypeError("Input must be an integer")
    return kilometers * METERS_PER_KILOMETER

if __name__ == '__main__':
    test_cases = [5, 12, 0, -3]
    for val in test_cases:
        print(convert_km_to_m(val))