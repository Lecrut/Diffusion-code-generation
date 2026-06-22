import math
import time

def calculate_rectangles_area(width, height, count):
    return [width * height for _ in range(count)]

def calculate_circles_area(radius, count):
    return [math.pi * radius ** 2 for _ in range(count)]

def benchmark_shapes():
    num_shapes = 10000
    width, height = 10.0, 20.0
    radius = 5.0

    start_rect = time.perf_counter()
    rects = calculate_rectangles_area(width, height, num_shapes)
    end_rect = time.perf_counter()
    rect_time = end_rect - start_rect

    start_circ = time.perf_counter()
    circles = calculate_circles_area(radius, num_shapes)
    end_circ = time.perf_counter()
    circ_time = end_circ - start_circ

    return {
        "rectangle_time": rect_time,
        "circle_time": circ_time,
        "sample_rectangle_area": rects[0],
        "sample_circle_area": circles[0]
    }

if __name__ == '__main__':
    results = benchmark_shapes()
    print(f"Rectangle Avg Time: {results['rectangle_time']}")
    print(f"Circle Avg Time: {results['circle_time']}")
    print(f"Sample Rectangle Area: {results['sample_rectangle_area']}")
    print(f"Sample Circle Area: {results['sample_circle_area']}")