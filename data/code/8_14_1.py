import sys
def calculate_polygon_area(coordinates):
    n = len(coordinates)
    area = 0.0
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2.0
if __name__ == '__main__':
    sample_coordinates = [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1)
    ]
    if not sample_coordinates:
        print("No coordinates provided.")
    else:
        area = calculate_polygon_area(sample_coordinates)
        print(f"{area}")