import time
import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def calculate_areas(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area

def benchmark_rectangles():
    rectangles = [Rectangle(1, 1) for _ in range(10000)]
    start_time = time.time()
    area = calculate_areas(rectangles)
    end_time = time.time()
    return end_time - start_time, area

def benchmark_circles():
    circles = [Circle(1) for _ in range(10000)]
    start_time = time.time()
    area = calculate_areas(circles)
    end_time = time.time()
    return end_time - start_time, area

if __name__ == '__main__':
    rect_time, rect_area = benchmark_rectangles()
    circle_time, circle_area = benchmark_circles()
    
    print(f"Rectangle calculation time: {rect_time:.6f} seconds")
    print(f"Total rectangle area: {rect_area}")
    
    print(f"Circle calculation time: {circle_time:.6f} seconds")
    print(f"Total circle area: {circle_area}")