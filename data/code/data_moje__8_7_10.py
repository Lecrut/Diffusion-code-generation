import time
import math
import random

def calculate_rectangles_area(widths, heights):
    areas = []
    for w, h in zip(widths, heights):
        areas.append(w * h)
    return areas

def calculate_circles_area(radii):
    areas = []
    for r in radii:
        areas.append(math.pi * r * r)
    return areas

def benchmark_area_calculations(n=10000, iterations=100):
    random.seed(42)
    widths = [random.uniform(1, 100) for _ in range(n)]
    heights = [random.uniform(1, 100) for _ in range(n)]
    radii = [random.uniform(1, 100) for _ in range(n)]

    start_time = time.perf_counter()
    for _ in range(iterations):
        rect_areas = calculate_rectangles_area(widths, heights)
    end_time = time.perf_counter()
    rect_time = (end_time - start_time) / iterations

    start_time = time.perf_counter()
    for _ in range(iterations):
        circ_areas = calculate_circles_area(radii)
    end_time = time.perf_counter()
    circ_time = (end_time - start_time) / iterations

    return {
        "rectangle_time_per_run": rect_time,
        "circle_time_per_run": circ_time,
        "speedup_factor": circ_time / rect_time if rect_time > 0 else float('inf')
    }

if __name__ == '__main__':
    results = benchmark_area_calculations()
    print("Rectangle calculation time (seconds):", results["rectangle_time_per_run"])
    print("Circle calculation time (seconds):", results["circle_time_per_run"])
    print("Circle vs Rectangle speedup factor:", results["speedup_factor"])