import math

def calculate_area_of_convex_hull(coordinates):
    n = len(coordinates)
    if n < 3:
        return 0.0
    
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        x_i, y_i = coordinates[i]
        x_j, y_j = coordinates[j]
        area += x_i * y_j - y_i * x_j
    
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_coordinates = [
        (0, 0),
        (4, 0),
        (4, 3),
        (0, 3)
    ]
    
    area = calculate_area_of_convex_hull(sample_coordinates)
    print(area)