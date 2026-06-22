import numpy as np

def calculate_polygon_area(points):
    if not isinstance(points, list) or len(points) < 3:
        raise ValueError("Points must be a list of at least three tuples representing vertices.")
    
    area = 0.5 * np.abs(np.dot(
        points[:, 0],
        np.roll(points[:, 1], 1)
    ) - np.dot(
        np.roll(points[:, 0], 1),
        points[:, 1]
    ))
    return area

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be a non-negative number.")
    
    return np.pi * radius ** 2

def compare_areas(polygon_points, circle_radius):
    polygon_area = calculate_polygon_area(polygon_points)
    circle_area = calculate_circle_area(circle_radius)
    
    comparison = "Polygon area is greater than Circle area" if polygon_area > circle_area else \
                 ("Polygon area is less than Circle area" if polygon_area < circle_area else 
                  "Areas are equal")
    return polygon_area, circle_area, comparison

if __name__ == '__main__':
    polygon_points = [(0, 0), (2, 0), (2, 2), (0, 2)]
    circle_radius = 1.5
    
    area_polygon, area_circle, comparison_result = compare_areas(polygon_points, circle_radius)
    
    print(f"Polygon points: {polygon_points}, Area Polygon: {area_polygon}")
    print(f"Circle radius: {circle_radius}, Area Circle: {area_circle}")
    print(comparison_result)