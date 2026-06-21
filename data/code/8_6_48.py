import time

class Shape:
    PI = 3.14159

    @staticmethod
    def calculate_rectangle_area(width, height):
        return width * height

    @staticmethod
    def calculate_circle_area(radius):
        return Shape.PI * radius * radius

def benchmark_shapes(rectangles, circles):
    start_time = time.time()
    
    total_area_rectangles = 0
    for width, height in rectangles:
        total_area_rectangles += Shape.calculate_rectangle_area(width, height)
    
    total_area_circles = 0
    for radius in circles:
        total_area_circles += Shape.calculate_circle_area(radius)
    
    end_time = time.time()
    
    return total_area_rectangles + total_area_circles, end_time - start_time

if __name__ == '__main__':
    rectangles = [(10, 20)] * 10000
    circles = [5] * 10000
    
    total_area, elapsed_time = benchmark_shapes(rectangles, circles)
    
    print(f"Total Area: {total_area}")
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")