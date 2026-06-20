import math

def scale_rectangle(width: float, height: float, scale: float) -> float:
    new_width = width * scale
    new_height = height * scale
    area = new_width * new_height
    return area

def scale_circle(radius: float, scale: float) -> float:
    new_radius = radius * scale
    area = math.pi * (new_radius ** 2)
    return area

def calculate_scaled_areas(rect_dims: dict, circle_dims: dict, scale: float) -> dict:
    rect_area = scale_rectangle(rect_dims['width'], rect_dims['height'], scale)
    circle_area = scale_circle(circle_dims['radius'], scale)
    return {
        'rectangle_area': rect_area,
        'circle_area': circle_area
    }

if __name__ == '__main__':
    rect_dimensions = {'width': 10.0, 'height': 5.0}
    circle_dimensions = {'radius': 4.0}
    scale_factor = 2.0

    results = calculate_scaled_areas(rect_dimensions, circle_dimensions, scale_factor)

    print(results['rectangle_area'])
    print(results['circle_area'])