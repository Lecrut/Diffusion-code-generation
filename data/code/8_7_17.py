import math
import time

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius * radius

def benchmark_geometry_operations(rect_count, circle_count):
    rect_areas = []
    start_time = time.perf_counter()
    for _ in range(rect_count):
        rect_areas.append(calculate_rectangle_area(10, 20))
    rect_elapsed = time.perf_counter() - start_time

    circle_areas = []
    start_time = time.perf_counter()
    for _ in range(circle_count):
        circle_areas.append(calculate_circle_area(10))
    circle_elapsed = time.perf_counter() - start_time

    return rect_elapsed, circle_elapsed, sum(rect_areas), sum(circle_areas)

if __name__ == '__main__':
    rect_elapsed, circle_elapsed, rect_sum, circle_sum = benchmark_geometry_operations(10000, 10000)
    print(f"Rectangle Time: {rect_elapsed:.6f}s, Total Area: {rect_sum}")
    print(f"Circle Time: {circle_elapsed:.6f}s, Total Area: {circle_sum}")