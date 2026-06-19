import math

def compare_areas(radius, side_length):
    circle_area = math.pi * radius ** 2
    square_area = side_length ** 2
    
    result = {
        'larger_figure': 'circle' if circle_area > square_area else 'square',
        'area_difference': abs(circle_area - square_area)
    }
    
    return result

if __name__ == '__main__':
    radius = 5
    side_length = 6
    comparison_result = compare_areas(radius, side_length)
    print(comparison_result)