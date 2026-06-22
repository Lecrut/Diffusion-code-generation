import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        raise ValueError('The list of coordinates cannot be empty.')
    
    points = np.array(coordinates)
    x_min, x_max = np.min(points[:, 0]), np.max(points[:, 0])
    y_min, y_max = np.min(points[:, 1]), np.max(points[:, 1])
    
    if x_max < x_min or y_max < y_min:
        raise ValueError('Invalid coordinates: bounding box dimensions cannot be negative.')
    
    width = x_max - x_min
    height = y_max - y_min
    
    return width * height

if __name__ == '__main__':
    sample_coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
    area = calculate_smallest_bounding_box_area(sample_coordinates)
    print(area)