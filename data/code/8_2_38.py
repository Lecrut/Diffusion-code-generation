import numpy as np

def calculate_min_bounding_box_area(coordinates):
    if not coordinates:
        return 0
    
    coords = np.array(coordinates)
    x_min, y_min = coords.min(axis=0)
    x_max, y_max = coords.max(axis=0)
    
    width = x_max - x_min
    height = y_max - y_min
    
    return width * height

if __name__ == '__main__':
    sample_coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
    area = calculate_min_bounding_box_area(sample_coordinates)
    print(area)