import time
import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def benchmark_rectangles(rectangles):
    start_time = time.time()
    total_area = sum(calculate_rectangle_area(rect['length'], rect['width']) for rect in rectangles)
    end_time = time.time()
    return total_area, end_time - start_time

def benchmark_circles(circles):
    start_time = time.time()
    total_area = sum(calculate_circle_area(circle['radius']) for circle in circles)
    end_time = time.time()
    return total_area, end_time - start_time

if __name__ == '__main__':
    rectangles = [{'length': 5, 'width': 10} for _ in range(10000)]
    circles = [{'radius': 3} for _ in range(10000)]

    rect_total_area, rect_time = benchmark_rectangles(rectangles)
    circle_total_area, circle_time = benchmark_circles(circles)

    print(f"Total area of rectangles: {rect_total_area}, Time taken: {rect_time:.6f} seconds")
    print(f"Total area of circles: {circle_total_area}, Time taken: {circle_time:.6f} seconds")