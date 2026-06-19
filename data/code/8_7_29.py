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
        return math.pi * self.radius ** 2

def calculate_areas(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area
if __name__ == '__main__':
    num_shapes = 10000
    rectangles = [Rectangle(2, 3) for _ in range(num_shapes)]
    circles = [Circle(1) for _ in range(num_shapes)]
    start_time = time.time()
    rectangle_area = calculate_areas(rectangles)
    end_time = time.time()
    print(f'Time to calculate area of {num_shapes} rectangles: {end_time - start_time:.6f} seconds')
    start_time = time.time()
    circle_area = calculate_areas(circles)
    end_time = time.time()
    print(f'Time to calculate area of {num_shapes} circles: {end_time - start_time:.6f} seconds')