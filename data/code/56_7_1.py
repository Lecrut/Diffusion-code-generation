import math
def compare_areas(radius, side_length):
    circle_area = math.pi * (radius ** 2)
    square_area = side_length ** 2
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
if __name__ == '__main__':
    circle_radius = 5.0
    square_side = 6.0
    result = compare_areas(circle_radius, square_side)
    print(result)