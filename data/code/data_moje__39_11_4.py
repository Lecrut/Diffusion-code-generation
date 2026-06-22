def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (25.5, 4),
        (0, 100),
        (12.5, 3.2)
    ]
    for area, height in test_cases:
        volume = calculate_prism_volume(area, height)
        print(f"Base Area: {area}, Height: {height}, Volume: {volume}")