import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

def compare_areas(radius, side_length):
    try:
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
    radius = 5
    side_length = 6
    result = compare_areas(radius, side_length)
    print(result)