def kilometers_to_miles(kilometers: float) -> float:
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number.")
    return kilometers * 0.621371

if __name__ == '__main__':
    test_cases = [
        (10.0, 6.21371),
        (5.0, 3.10686),
        (0.0, 0.0),
        (-1.0, -0.621371)
    ]
    
    for kilometers, expected in test_cases:
        result = kilometers_to_miles(kilometers)
        print(f"{kilometers} km is {result:.5f} miles (Expected: {expected:.5f})")