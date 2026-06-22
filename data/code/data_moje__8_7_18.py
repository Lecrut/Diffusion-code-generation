import math
import time

def calculate_area_rect(width, height):
    return width * height

def calculate_area_circle(radius):
    return math.pi * radius * radius

def benchmark_calculations(num_items, rect_width, rect_height, circle_radius):
    total_area_rect = 0.0
    total_area_circle = 0.0
    
    start_time = time.perf_counter()
    for _ in range(num_items):
        total_area_rect += calculate_area_rect(rect_width, rect_height)
    end_time = time.perf_counter()
    time_rect = end_time - start_time
    
    start_time = time.perf_counter()
    for _ in range(num_items):
        total_area_circle += calculate_area_circle(circle_radius)
    end_time = time.perf_counter()
    time_circle = end_time - start_time
    
    return total_area_rect, total_area_circle, time_rect, time_circle

if __name__ == '__main__':
    num_items = 10000
    rect_width = 10.0
    rect_height = 20.0
    circle_radius = 10.0
    
    area_rect, area_circle, time_rect, time_circle = benchmark_calculations(
        num_items, rect_width, rect_height, circle_radius
    )
    
    print(f"{time_rect:.6f}")
    print(f"{time_circle:.6f}")
    print(f"{area_rect}")
    print(f"{area_circle}")