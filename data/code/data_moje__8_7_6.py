import math
import time

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def benchmark_geometry_operations(rect_count, circle_count):
    width, height = 10.0, 20.0
    radius = 5.0

    start_time = time.perf_counter()
    rect_areas = [calculate_rectangle_area(width, height) for _ in range(rect_count)]
    end_time = time.perf_counter()
    rect_time = end_time - start_time

    start_time = time.perf_counter()
    circle_areas = [calculate_circle_area(radius) for _ in range(circle_count)]
    end_time = time.perf_counter()
    circle_time = end_time - start_time

    total_rect_area = sum(rect_areas)
    total_circle_area = sum(circle_areas)

    return {
        "rect_count": rect_count,
        "circle_count": circle_count,
        "rect_time_seconds": rect_time,
        "circle_time_seconds": circle_time,
        "total_rect_area": total_rect_area,
        "total_circle_area": total_circle_area
    }

if __name__ == '__main__':
    N = 10000
    results = benchmark_geometry_operations(N, N)
    print(results)