import time

class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

def calculate_areas(shapes):
    total_area = 0
    for shape in shapes:
        if not hasattr(shape, 'area'):
            raise ValueError("All shapes must have an 'area' method")
        total_area += shape.area()
    return total_area

def benchmark_shapes(rectangles, circles):
    start_time = time.time()

    rectangles = [Rectangle(width, height) for width, height in rectangles]
    circles = [Circle(radius) for radius in circles]

    total_area_rectangles = calculate_areas(rectangles)
    total_area_circles = calculate_areas(circles)

    end_time = time.time()
    return total_area_rectangles + total_area_circles, end_time - start_time

if __name__ == '__main__':
    rectangles = [(10, 20)] * 10000
    circles = [5] * 10000

    total_area, elapsed_time = benchmark_shapes(rectangles, circles)
    print(f"Total Area: {total_area}")
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")