import numpy as np

def polygon_area(points):
    x = points[:, 0]
    y = points[:, 1]
    area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    return area

def circle_area(radius):
    return np.pi * radius ** 2

if __name__ == '__main__':
    polygon_points = np.array([(0, 0), (2, 0), (2, 2), (0, 2)])
    circle_radius = 1.5
    
    polygon_area_result = polygon_area(polygon_points)
    circle_area_result = circle_area(circle_radius)
    
    print(f"Polygon area: {polygon_area_result}")
    print(f"Circle area: {circle_area_result}")
    comparison = "Polygon area is greater than circle area" if polygon_area_result > circle_area_result else ("Polygon area is less than circle area" if polygon_area_result < circle_area_result else "Areas are equal")
    print(comparison)