def km_to_miles(km: float) -> float:
    if not isinstance(km, (int, float)):
        raise ValueError("Invalid input type. Please provide a number.")
    return km * 0.621371

if __name__ == '__main__':
    test_cases = [
        (10.0, 6.21371),
        (50.0, 31.06855),
        (0.0, 0.0),
        (-5.0, -3.106855)
    ]
    
    for km, expected in test_cases:
        result = km_to_miles(km)
        print(f"km_to_miles({km}) -> {result}, Expected: {expected}")