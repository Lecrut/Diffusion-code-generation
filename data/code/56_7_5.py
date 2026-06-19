import math

def validate_positive(value):
    if value <= 0:
        raise ValueError("Value must be positive")

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_square_area(side_length):
    return side_length ** 2

def compare_areas(radius, side_length):
    try:
        validate_positive(radius)
        validate_positive(side_length)
        
        circle_area = calculate_circle_area(radius)
        square_area = calculate_square_area(side_length)
        
        if circle_area > square_area:
            larger_figure = "circle"
            difference = circle_area - square_area
        elif square_area > circle_area:
            larger_figure = "square"
            difference = square_area - circle_area
        else:
            larger_figure = "equal"
            difference = 0.0
        
        return {
            "circle_area": circle_area,
            "square_area": square_area,
            "larger_figure": larger_figure,
            "difference": difference
        }
    except ValueError as e:
        return {"error": str(e)}

if __name__ == '__main__':
    radius = 7.0
    side_length = 5.0
    result = compare_areas(radius, side_length)
    print(result)