class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self) -> float:
        import math
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    rect = Rectangle(5.0, 10.0)
    circle = Circle(3.0)
    
    print(f"Rectangle area with dimensions {rect.width}x{rect.height}: {rect.calculate_area()}")
    print(f"Circle area with radius {circle.radius}: {circle.calculate_area():.2f}")