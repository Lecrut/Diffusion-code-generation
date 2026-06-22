import numpy as np

def smallest_bounding_box_area(points):
    if not points:
        return 0
    
    x_coords, y_coords = zip(*points)
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    
    width = max_x - min_x
    height = max_y - min_y
    
    return width * height

if __name__ == '__main__':
    sample_points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    area = smallest_bounding_box_area(sample_points)
    print(area)