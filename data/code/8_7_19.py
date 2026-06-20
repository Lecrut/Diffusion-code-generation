import time
import math

PI = math.pi

def calculate_rectangles_area(width, height, count):
    total_area = 0.0
    for _ in range(count):
        total_area += width * height
    return total_area

def calculate_circles_area(radius, count):
    total_area = 0.0
    for _ in range(count):
        total_area += PI * radius * radius
    return total_area

def run_benchmark():
    count = 10000
    rect_width = 10.0
    rect_height = 20.0
    circle_radius = 15.0

    start_rect = time.perf_counter()
    rect_total = calculate_rectangles_area(rect_width, rect_height, count)
    end_rect = time.perf_counter()
    rect_duration = end_rect - start_rect

    start_circ = time.perf_counter()
    circ_total = calculate_circles_area(circle_radius, count)
    end_circ = time.perf_counter()
    circ_duration = end_circ - start_circ

    print(f"Rectangle Total Area: {rect_total}")
    print(f"Rectangle Time: {rect_duration:.6f}s")
    print(f"Circle Total Area: {circ_total}")
    print(f"Circle Time: {circ_duration:.6f}s")

if __name__ == '__main__':
    run_benchmark()