import time
import math

def calculate_rectangle_area(rectangles):
    total_area = 0
    for rect in rectangles:
        width, height = rect
        total_area += width * height
    return total_area

def calculate_circle_area(circles):
    total_area = 0
    for circle in circles:
        radius = circle[0]
        total_area += math.pi * (radius ** 2)
    return total_area

def benchmark():
    rectangles = [(1, 2) for _ in range(10000)]
    circles = [(3,) for _ in range(10000)]

    start_time = time.time()
    rect_area = calculate_rectangle_area(rectangles)
    rect_time = time.time() - start_time

    start_time = time.time()
    circle_area = calculate_circle_area(circles)
    circle_time = time.time() - start_time

    print(f"Rectangle area: {rect_area}, Time taken: {rect_time:.6f} seconds")
    print(f"Circle area: {circle_area}, Time taken: {circle_time:.6f} seconds")

if __name__ == '__main__':
    benchmark()