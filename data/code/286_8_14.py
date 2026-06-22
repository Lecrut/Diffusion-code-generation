def validate_km_to_miles(value: float) -> None:
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number.")

def km_to_miles(km: float) -> float:
    validate_km_to_miles(km)
    return km * 0.621371

if __name__ == '__main__':
    test_cases = [
        (10.0, 6.21371),
        (50.0, 31.06855),
        (0.0, 0.0),
        (1.0, 0.621371)
    ]

    for km, expected in test_cases:
        result = km_to_miles(km)
        print(f"{km} km is {result:.5f} miles (Expected: {expected:.5f})")