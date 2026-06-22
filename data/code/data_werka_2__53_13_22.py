def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    test_areas = {
        'small_square': 16,
        'medium_square': 25,
        'large_square': 81
    }
    
    for name, area in test_areas.items():
        side_length = calculate_square_side_length(area)
        print(f"The side length of the {name} is: {side_length}")