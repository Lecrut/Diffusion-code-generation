def calculate_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (15.5, 4),
        (0, 100),
        (25, 0),
        (100, 2.5)
    ]

    for area, height in test_cases:
        volume = calculate_prism_volume(area, height)
        print(f"Base Area: {area}, Height: {height}, Volume: {volume}")