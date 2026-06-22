import math
import time

def calculate_rectangles_area(width: float, height: float, count: int) -> float:
    total_area = 0.0
    for _ in range(count):
        total_area += width * height
    return total_area

def calculate_circles_area(radius: float, count: int) -> float:
    total_area = 0.0
    for _ in range(count):
        total_area += math.pi * radius * radius
    return total_area

def benchmark(func, *args, iterations: int = 10) -> float:
    total_time = 0.0
    for _ in range(iterations):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        total_time += end - start
    return total_time / iterations

def run_benchmarks():
    count = 10000
    width = 10.0
    height = 5.0
    radius = 5.0
    
    rect_time = benchmark(calculate_rectangles_area, width, height, count)
    circle_time = benchmark(calculate_circles_area, radius, count, iterations=50)
    
    rect_result = calculate_rectangles_area(width, height, count)
    circle_result = calculate_circles_area(radius, count)
    
    print(f"Rectangle Area: {rect_result}")
    print(f"Rectangle Time: {rect_time}")
    print(f"Circle Area: {circle_result}")
    print(f"Circle Time: {circle_time}")

if __name__ == '__main__':
    run_benchmarks()