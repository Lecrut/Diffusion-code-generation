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
    rectangles_total_area = calculate_areas(rectangles)
    circles_total_area = calculate_areas(circles)
    end_time = time.time()
    return (rectangles_total_area + circles_total_area), end_time - start_time

if __name__ == '__main__':
    rectangles = [Rectangle(10, 20) for _ in range(10000)]
    circles = [Circle(5) for _ in range(10000)]

    total_area, elapsed_time = benchmark_shapes(rectangles, circles)
    print(f"Total Area: {total_area}")
    print(f"Elapsed Time: {elapsed_time} seconds")