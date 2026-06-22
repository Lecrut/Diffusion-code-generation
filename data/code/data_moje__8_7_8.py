import math
import time

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius * radius

def benchmark_areas(n=10000, num_runs=100):
    rect_widths = [float(i + 1) for i in range(n)]
    rect_heights = [float(i + 1) for i in range(n)]
    circle_radii = [float(i + 1) for i in range(n)]

    rect_times = []
    for _ in range(num_runs):
        start = time.perf_counter()
        total_rect_area = 0.0
        for i in range(n):
            total_rect_area += calculate_rectangle_area(rect_widths[i], rect_heights[i])
        end = time.perf_counter()
        rect_times.append(end - start)

    circle_times = []
    for _ in range(num_runs):
        start = time.perf_counter()
        total_circle_area = 0.0
        for i in range(n):
            total_circle_area += calculate_circle_area(circle_radii[i])
        end = time.perf_counter()
        circle_times.append(end - start)

    avg_rect_time = sum(rect_times) / len(rect_times)
    avg_circle_time = sum(circle_times) / len(circle_times)

    return {
        "rectangles_avg_time": avg_rect_time,
        "circles_avg_time": avg_circle_time,
        "rectangles_ratio": avg_rect_time / avg_circle_time if avg_circle_time > 0 else 0
    }

if __name__ == '__main__':
    result = benchmark_areas(n=10000, num_runs=100)
    print(result["rectangles_avg_time"])
    print(result["circles_avg_time"])
    print(result["rectangles_ratio"])