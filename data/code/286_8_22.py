def km_to_miles(km: float) -> float:
    return km * 0.621371

if __name__ == '__main__':
    test_cases = [
        (10.0, 6.21371),
        (5.0, 3.10686),
        (0.0, 0.0),
        (1.0, 0.621371),
        (100.0, 62.1371)
    ]

    for km, expected in test_cases:
        result = km_to_miles(km)
        print(f"{km} km is {result:.5f} miles (Expected: {expected:.5f})")