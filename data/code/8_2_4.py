class Shape:
    """Base class representing a geometric shape."""
    
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    """Class representing a rectangle that calculates its area."""
    
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    
    def calculate_area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    """Class representing a circle that calculates its area."""
    
    PI = 3.141592653589793
    
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def calculate_area(self) -> float:
        return Circle.PI * (self.radius ** 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    rect_width = 5.0
    rect_height = 3.0
    circle_radius = 4.0

    rectangle = Rectangle(rect_width, rect_height)
    circle = Circle(circle_radius)

    print(f"Rectangle Area: {rectangle.calculate_area()}")
    print(f"Circle Area: {circle.calculate_area()}")