import math

def validate_area(area):
    if not isinstance(area, (int, float)):
        raise TypeError("Area must be a number")
    if area < 0:
        raise ValueError("Area cannot be negative")

def calculate_square_side_length(area):
    validate_area(area)
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = [
        {'description': 'small', 'area': 9.0},
        {'description': 'medium', 'area': 16.0},
        {'description': 'large', 'area': 25.0}
    ]
    
    for item in sample_areas:
        try:
            side_length = calculate_square_side_length(item['area'])
            print(f"The side length of the {item['description']} square is: {side_length}")
        except (ValueError, TypeError) as e:
            print(e)