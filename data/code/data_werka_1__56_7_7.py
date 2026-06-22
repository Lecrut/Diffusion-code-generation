import math

def compare_areas(radius, side_length):
    circle_area = math.pi * radius ** 2
    square_area = side_length ** 2
    
    result = {
        'figure': 'circle' if circle_area > square_area else 'square',
        'difference': abs(circle_area - square_area)
    }
    
    return result

if __name__ == '__main__':
    sample_radius = 5
    sample_side_length = 6
    comparison_result = compare_areas(sample_radius, sample_side_length)
    print(comparison_result)