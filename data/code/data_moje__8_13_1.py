import math

def calculate_scaled_areas(rectangles, circles, scale_factor):
    results = []
    for width, height in rectangles:
        original_area = width * height
        scaled_width = width * scale_factor
        scaled_height = height * scale_factor
        scaled_area = scaled_width * scaled_height
        results.append(('rectangle', original_area, scaled_area))
    for radius, in circles:
        original_area = math.pi * radius ** 2
        scaled_radius = radius * scale_factor
        scaled_area = math.pi * scaled_radius ** 2
        results.append(('circle', original_area, scaled_area))
    return results
if __name__ == '__main__':
    sample_rectangles = [(3.0, 4.0), (5.5, 2.0), (10.0, 10.0)]
    sample_circles = [(2.5,), (7.0,), (1.0,)]
    sample_scale_factor = 2.5
    results = calculate_scaled_areas(sample_rectangles, sample_circles, sample_scale_factor)
    for shape_type, original_area, scaled_area in results:
        print(f'{shape_type}: original_area={original_area}, scaled_area={scaled_area}')