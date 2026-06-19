import numpy as np

def calculate_min_bounding_box_area(coordinates):
    if not coordinates:
        return 0.0
    
    x_coords, y_coords = zip(*coordinates)
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    
    width = max_x - min_x
    height = max_y - min_y
    
    return width * height

if __name__ == '__main__':
    sample_coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
    area = calculate_min_bounding_box_area(sample_coordinates)
    print(area)