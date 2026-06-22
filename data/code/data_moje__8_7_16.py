import math
import time

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def benchmark(func, *args, iterations=10000):
    start_time = time.perf_counter()
    for _ in range(iterations):
        result = func(*args)
    end_time = time.perf_counter()
    return end_time - start_time, result

if __name__ == '__main__':
    rect_width = 10.0
    rect_height = 20.0
    circle_radius = 15.0

    rect_time, rect_result = benchmark(calculate_rectangle_area, rect_width, rect_height)
    circle_time, circle_result = benchmark(calculate_circle_area, circle_radius)

    print(f"Rectangle Area: {rect_result}, Time: {rect_time:.6f}s")
    print(f"Circle Area: {circle_result}, Time: {circle_time:.6f}s")