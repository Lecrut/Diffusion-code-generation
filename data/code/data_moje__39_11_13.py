def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    test_cases = [
        (10.0, 5.0),
        (25.5, 3.2),
        (100, 10),
        (0, 50),
        (7.5, 4.0)
    ]
    for base, height in test_cases:
        volume = calculate_prism_volume(base, height)
        print(f"Base: {base}, Height: {height}, Volume: {volume}")