import math
import time

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def benchmark_area_calculations():
    num_shapes = 10000
    dimensions_rect = [10.0, 20.0]
    radius_circle = 5.0

    start_time = time.time()
    rect_areas = []
    for _ in range(num_shapes):
        rect_areas.append(calculate_rectangle_area(*dimensions_rect))
    end_time = time.time()
    rect_time = end_time - start_time
    rect_total = sum(rect_areas)

    start_time = time.time()
    circle_areas = []
    for _ in range(num_shapes):
        circle_areas.append(calculate_circle_area(radius_circle))
    end_time = time.time()
    circle_time = end_time - start_time
    circle_total = sum(circle_areas)

    return {
        "rectangle_total": rect_total,
        "rectangle_time": rect_time,
        "circle_total": circle_total,
        "circle_time": circle_time
    }

if __name__ == '__main__':
    results = benchmark_area_calculations()
    print(results)