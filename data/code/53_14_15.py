import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = {
        'small': 9.0,
        'medium': 16.0,
        'large': 25.0
    }
    
    for description, area in sample_areas.items():
        try:
            side_length = calculate_square_side_length(area)
            print(f"The side length of the {description} square is: {side_length:.2f}")
        except ValueError as e:
            print(e)