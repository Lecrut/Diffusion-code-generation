import time
import math

def calculate_rectangles_area(count):
    total_area = 0.0
    for i in range(count):
        width = 1.0 + (i % 10) * 0.5
        height = 2.0 + (i % 7) * 0.3
        total_area += width * height
    return total_area

def calculate_circles_area(count):
    total_area = 0.0
    for i in range(count):
        radius = 1.0 + (i % 12) * 0.4
        total_area += math.pi * radius * radius
    return total_area

if __name__ == '__main__':
    sample_rect_count = 10000
    sample_circle_count = 10000

    start_time = time.perf_counter()
    rect_area = calculate_rectangles_area(sample_rect_count)
    rect_duration = time.perf_counter() - start_time

    start_time = time.perf_counter()
    circle_area = calculate_circles_area(sample_circle_count)
    circle_duration = time.perf_counter() - start_time

    print(f"Rectangles: Area={rect_area:.4f}, Time={rect_duration:.6f}s")
    print(f"Circles: Area={circle_area:.4f}, Time={circle_duration:.6f}s")