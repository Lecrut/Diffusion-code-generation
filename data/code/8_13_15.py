import math

def calculate_scaled_areas(rectangles, circles, scale_factor):
    scaled_rect_areas = []
    for width, height in rectangles:
        scaled_width = width * scale_factor
        scaled_height = height * scale_factor
        area = scaled_width * scaled_height
        scaled_rect_areas.append(area)

    scaled_circle_areas = []
    for radius in circles:
        scaled_radius = radius * scale_factor
        area = math.pi * (scaled_radius ** 2)
        scaled_circle_areas.append(area)

    return scaled_rect_areas, scaled_circle_areas

if __name__ == '__main__':
    rectangles = [(2.0, 3.0), (5.0, 5.0), (1.5, 4.0)]
    circles = [1.0, 2.5, 3.0]
    scale_factor = 2.0

    rect_areas, circle_areas = calculate_scaled_areas(rectangles, circles, scale_factor)
    print(rect_areas)
    print(circle_areas)