import math
import time

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def benchmark_shapes(num_shapes):
    start_time = time.perf_counter()
    rectangle_areas = [calculate_rectangle_area(10.5, 20.2) for _ in range(num_shapes)]
    end_time = time.perf_counter()
    rectangle_time = end_time - start_time

    start_time = time.perf_counter()
    circle_areas = [calculate_circle_area(10.0) for _ in range(num_shapes)]
    end_time = time.perf_counter()
    circle_time = end_time - start_time

    total_rectangle_area = sum(rectangle_areas)
    total_circle_area = sum(circle_areas)

    return {
        "rectangle_count": num_shapes,
        "rectangle_total_area": total_rectangle_area,
        "rectangle_elapsed_seconds": rectangle_time,
        "circle_count": num_shapes,
        "circle_total_area": total_circle_area,
        "circle_elapsed_seconds": circle_time
    }

if __name__ == '__main__':
    results = benchmark_shapes(10000)
    print(results)