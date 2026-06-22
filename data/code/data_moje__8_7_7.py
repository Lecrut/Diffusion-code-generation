import time
import math

def calculate_rectangles_area(width, height, count):
    start_time = time.perf_counter()
    total_area = 0.0
    for _ in range(count):
        total_area += width * height
    end_time = time.perf_counter()
    return total_area, end_time - start_time

def calculate_circles_area(radius, count):
    start_time = time.perf_counter()
    total_area = 0.0
    for _ in range(count):
        total_area += math.pi * radius * radius
    end_time = time.perf_counter()
    return total_area, end_time - start_time

if __name__ == '__main__':
    rect_area, rect_time = calculate_rectangles_area(10.0, 20.0, 10000)
    circ_area, circ_time = calculate_circles_area(10.0, 10000)
    print(f"Rectangles Total Area: {rect_area}")
    print(f"Rectangles Time: {rect_time}")
    print(f"Circles Total Area: {circ_area}")
    print(f"Circles Time: {circ_time}")