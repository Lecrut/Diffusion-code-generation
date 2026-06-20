import time
import math
import random

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def benchmark_shapes(num_iterations=10000):
    random.seed(42)
    widths = [random.uniform(1, 100) for _ in range(num_iterations)]
    heights = [random.uniform(1, 100) for _ in range(num_iterations)]
    radii = [random.uniform(1, 50) for _ in range(num_iterations)]

    start_rect = time.perf_counter()
    rect_areas = [calculate_rectangle_area(w, h) for w, h in zip(widths, heights)]
    end_rect = time.perf_counter()
    rect_time = end_rect - start_rect

    start_circ = time.perf_counter()
    circ_areas = [calculate_circle_area(r) for r in radii]
    end_circ = time.perf_counter()
    circ_time = end_circ - start_circ

    return {
        "rectangle_time": rect_time,
        "circle_time": circ_time,
        "rect_sum_area": sum(rect_areas),
        "circ_sum_area": sum(circ_areas),
        "num_iterations": num_iterations
    }

if __name__ == '__main__':
    results = benchmark_shapes(10000)
    print(results["rectangle_time"])
    print(results["circle_time"])
    print(results["rect_sum_area"])
    print(results["circ_sum_area"])