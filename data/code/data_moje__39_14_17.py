def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_cases = [
        {"base_area": 25, "height": 10, "expected": 250},
        {"base_area": 14.5, "height": 6, "expected": 87.0},
        {"base_area": 100, "height": 5, "expected": 500}
    ]
    
    for case in test_cases:
        base_area = case["base_area"]
        height = case["height"]
        result = calculate_prism_volume(base_area, height)
        print(f"Base Area: {base_area}, Height: {height}, Volume: {result}")