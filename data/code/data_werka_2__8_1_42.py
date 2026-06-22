import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        raise ValueError('The list of coordinates cannot be empty.')
    
    x_coords, y_coords = zip(*coordinates)
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    
    width = max_x - min_x
    height = max_y - min_y
    
    if width < 0 or height < 0:
        raise ValueError('Invalid coordinates: bounding box dimensions cannot be negative.')
    
    area = width * height
    return area

if __name__ == '__main__':
    sample_coordinates = [(2, 3), (5, 7), (1, 4), (6, 8)]
    try:
        area = calculate_smallest_bounding_box_area(sample_coordinates)
        print(area)
    except ValueError as e:
        print(e)