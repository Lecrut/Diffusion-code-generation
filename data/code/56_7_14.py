import math

def validate_input(radius, side_length):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_square_area(side_length):
    return side_length ** 2

def compare_areas(radius, side_length):
    validate_input(radius, side_length)
    
    circle_area = calculate_circle_area(radius)
    square_area = calculate_square_area(side_length)
    
    if circle_area > square_area:
        larger_figure = "circle"
        difference = circle_area - square_area
    else:
        larger_figure = "square"
        difference = square_area - circle_area
    
    return {
        "circle_area": circle_area,
        "square_area": square_area,
        "larger_figure": larger_figure,
        "difference": difference
    }

if __name__ == '__main__':
    radius = 7
    side_length = 4
    result = compare_areas(radius, side_length)
    print(result)