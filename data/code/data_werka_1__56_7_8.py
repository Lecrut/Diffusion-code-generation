import math

def compare_areas(radius, side_length):
    circle_area = math.pi * radius ** 2
    square_area = side_length ** 2
    
    result = {}
    if circle_area > square_area:
        result['larger_figure'] = 'circle'
        result['difference'] = circle_area - square_area
    else:
        result['larger_figure'] = 'square'
        result['difference'] = square_area - circle_area
    
    return result

if __name__ == '__main__':
    radius = 5
    side_length = 4
    print(compare_areas(radius, side_length))