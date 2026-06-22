def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (25.5, 8),
        (0, 100),
        (12.5, 4.2)
    ]
    for base, h in test_cases:
        volume = calculate_prism_volume(base, h)
        print(f"Base Area: {base}, Height: {h}, Volume: {volume}")