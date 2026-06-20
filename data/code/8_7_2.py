import time
import math

def calculate_rectangles_area(width, height, count):
    total = 0.0
    for _ in range(count):
        total += width * height
    return total

def calculate_circles_area(radius, count):
    total = 0.0
    for _ in range(count):
        total += math.pi * radius * radius
    return total

if __name__ == '__main__':
    rect_width = 5
    rect_height = 10
    circle_radius = 7
    iterations = 10000

    start_time = time.perf_counter()
    rect_area = calculate_rectangles_area(rect_width, rect_height, iterations)
    rect_duration = time.perf_counter() - start_time

    start_time = time.perf_counter()
    circle_area = calculate_circles_area(circle_radius, iterations)
    circle_duration = time.perf_counter() - start_time

    print(f"Rectangles total area: {rect_area}")
    print(f"Rectangles duration: {rect_duration}")
    print(f"Circles total area: {circle_area}")
    print(f"Circles duration: {circle_duration}")
    print(f"Efficiency ratio (Circle/Rect time): {circle_duration / rect_duration}")