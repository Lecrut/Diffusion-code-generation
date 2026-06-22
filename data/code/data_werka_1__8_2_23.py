import numpy as np

def calculate_min_bounding_box_area(points):
    if not points:
        return 0
    
    x_coords, y_coords = zip(*points)
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    
    width = max_x - min_x
    height = max_y - min_y
    
    return width * height

if __name__ == '__main__':
    sample_points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    area = calculate_min_bounding_box_area(sample_points)
    print(area)