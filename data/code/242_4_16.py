import numpy as np

def calculate_polygon_area(points):
    x = points[:, 0]
    y = points[:, 1]
    area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    return area

def compare_areas(polygon_points, circle_radius):
    polygon_area = calculate_polygon_area(polygon_points)
    circle_area = np.pi * (circle_radius ** 2)
    comparison = "Polygon area is greater" if polygon_area > circle_area else ("Circle area is greater" if polygon_area < circle_area else "Areas are equal")
    return polygon_area, circle_area, comparison

if __name__ == '__main__':
    polygon_points = np.array([(0,0), (2,0), (2,2), (0,2)])
    circle_radius = 1.5
    polygon_area, circle_area, comparison_result = compare_areas(polygon_points, circle_radius)
    print(f"Polygon area: {polygon_area}")
    print(f"Circle area: {circle_area}")
    print(comparison_result)