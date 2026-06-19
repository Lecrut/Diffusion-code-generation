import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        return 0
    
    coords = np.array(coordinates)
    x_min, y_min = np.min(coords, axis=0)
    x_max, y_max = np.max(coords, axis=0)
    
    width = x_max - x_min
    height = y_max - y_min
    
    area = width * height
    return area

if __name__ == '__main__':
    sample_coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
    print(calculate_smallest_bounding_box_area(sample_coordinates))