import math

class ShapeAreaComparer:
    def __init__(self):
        self.circle_radius = 5.0
        self.rectangle_length = 10.0
        self.rectangle_width = 2.0
    
    def calculate_circle_area(self):
        return math.pi * self.circle_radius**2
    
    def calculate_rectangle_area(self):
        return self.rectangle_length * self.rectangle_width
    
    def are_areas_equal(self, epsilon=1e-9):
        circle_area = self.calculate_circle_area()
        rectangle_area = self.calculate_rectangle_area()
        return abs(circle_area - rectangle_area) < epsilon

if __name__ == '__main__':
    comparer = ShapeAreaComparer()
    print("Circle Area:", comparer.calculate_circle_area())
    print("Rectangle Area:", comparer.calculate_rectangle_area())
    if comparer.are_areas_equal():
        print("The areas are equal.")
    else:
        print("The areas are not equal.")