import time
import math

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius * radius

def benchmark_areas():
    rectangle_count = 10000
    circle_count = 10000
    
    rectangle_width = 5.0
    rectangle_height = 10.0
    circle_radius = 7.0
    
    start_time = time.perf_counter()
    for _ in range(rectangle_count):
        calculate_rectangle_area(rectangle_width, rectangle_height)
    rectangle_time = time.perf_counter() - start_time
    
    start_time = time.perf_counter()
    for _ in range(circle_count):
        calculate_circle_area(circle_radius)
    circle_time = time.perf_counter() - start_time
    
    print(f"Rectangle area: {calculate_rectangle_area(rectangle_width, rectangle_height)}")
    print(f"Circle area: {calculate_circle_area(circle_radius)}")
    print(f"Time for 10000 rectangles: {rectangle_time:.6f} seconds")
    print(f"Time for 10000 circles: {circle_time:.6f} seconds")

if __name__ == '__main__':
    benchmark_areas()