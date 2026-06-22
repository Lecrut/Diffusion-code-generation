import time

class Shape:
    PI = 3.14159

    @staticmethod
    def rectangle_area(width, height):
        return width * height

    @staticmethod
    def circle_area(radius):
        return Shape.PI * radius * radius

def calculate_areas(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape()
    return total_area

def benchmark_shapes(rectangles, circles):
    start_time = time.time()
    rectangles_area = calculate_areas([lambda: Shape.rectangle_area(w, h) for w, h in rectangles])
    circles_area = calculate_areas([lambda: Shape.circle_area(r) for r in circles])
    end_time = time.time()
    return rectangles_area + circles_area, end_time - start_time

if __name__ == '__main__':
    rectangles = [(10, 20)] * 10000
    circles = [5] * 10000
    total_area, elapsed_time = benchmark_shapes(rectangles, circles)
    print(f"Total Area: {total_area}")
    print(f"Elapsed Time: {elapsed_time} seconds")