import numpy as np

def smallest_bounding_box_area(coordinates):
    if not coordinates:
        return 0
    
    coords = np.array(coordinates)
    min_x, min_y = coords.min(axis=0)
    max_x, max_y = coords.max(axis=0)
    
    width = max_x - min_x
    height = max_y - min_y
    
    return width * height

if __name__ == '__main__':
    sample_coords = [(1, 2), (3, 4), (5, 6), (7, 8)]
    area = smallest_bounding_box_area(sample_coords)
    print(area)