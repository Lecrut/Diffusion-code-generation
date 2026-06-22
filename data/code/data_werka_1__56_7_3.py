import math

def compare_areas(radius, side_length):
    circle_area = math.pi * radius ** 2
    square_area = side_length ** 2
    
    if circle_area > square_area:
        return {
            'larger_figure': 'circle',
            'difference': circle_area - square_area
        }
    else:
        return {
            'larger_figure': 'square',
            'difference': square_area - circle_area
        }

if __name__ == '__main__':
    radius = 5
    side_length = 6
    result = compare_areas(radius, side_length)
    print(result)