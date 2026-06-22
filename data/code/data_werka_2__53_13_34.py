def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

def validate_area(area):
    if not isinstance(area, (int, float)):
        raise TypeError("Area must be a number")
    if area < 0:
        raise ValueError("Area cannot be negative")

if __name__ == '__main__':
    sample_areas = {
        'tiny_square': 9,
        'medium_square': 49,
        'large_square': 169
    }
    
    for name, area in sample_areas.items():
        validate_area(area)
        side_length = calculate_square_side_length(area)
        print(f"The side length of the {name} is: {side_length}")