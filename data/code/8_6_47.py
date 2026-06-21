import time

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
        return 3.14159 * self.radius * self.radius

def calculate_areas(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area

def benchmark_shapes(rectangles, circles):
    start_time = time.time()
    
    rectangle_objects = [Rectangle(width, height) for width, height in rectangles]
    circle_objects = [Circle(radius) for radius in circles]
    
    total_area_rectangles = calculate_areas(rectangle_objects)
    total_area_circles = calculate_areas(circle_objects)
    
    end_time = time.time()
    
    return total_area_rectangles + total_area_circles, end_time - start_time

if __name__ == '__main__':
    rectangles = [(10, 20)] * 10000
    circles = [5] * 10000
    
    total_area, elapsed_time = benchmark_shapes(rectangles, circles)
    
    print(f"Total Area: {total_area}")
    print(f"Elapsed Time: {elapsed_time} seconds")