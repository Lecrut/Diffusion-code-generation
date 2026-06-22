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
        return 3.14159 * self.radius ** 2

def calculate_areas(rectangles, circles):
    rect_areas = [rect.area() for rect in rectangles]
    circle_areas = [circle.area() for circle in circles]
    return (rect_areas, circle_areas)
if __name__ == '__main__':
    num_rectangles = 10000
    num_circles = 10000
    rectangles = [Rectangle(2.5, 3.5) for _ in range(num_rectangles)]
    circles = [Circle(4.5) for _ in range(num_circles)]
    start_time = time.time()
    rect_areas, circle_areas = calculate_areas(rectangles, circles)
    end_time = time.time()
    print(f'Time taken to calculate areas: {end_time - start_time:.6f} seconds')
    print(f'Total area of rectangles: {sum(rect_areas):.2f}')
    print(f'Total area of circles: {sum(circle_areas):.2f}')