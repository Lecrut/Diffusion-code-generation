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

def calculate_area(rectangles, circles):
    start_time = time.time()
    
    total_area = 0
    for rect in rectangles:
        total_area += rect.area()
    
    for circ in circles:
        total_area += circ.area()
    
    end_time = time.time()
    return total_area, end_time - start_time

if __name__ == '__main__':
    rectangles = [Rectangle(10, 20) for _ in range(10000)]
    circles = [Circle(5) for _ in range(10000)]
    
    total_area, elapsed_time = calculate_area(rectangles, circles)
    print(f"Total Area: {total_area}")
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")