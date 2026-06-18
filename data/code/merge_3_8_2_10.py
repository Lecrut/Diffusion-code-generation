class Shape:
    """Base class representing a geometric shape with an area calculation method."""
    
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    """Class representing a rectangle that calculates its area based on width and height."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    """Class representing a circle that calculates its area based on radius."""

    PI = 3.141592653589793
    
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return Circle.PI * (self.radius ** 2)

if __name__ == '__main__':
    # Sample values for testing the Shape hierarchy and area calculations
    
    rect_width = 5.0
    rect_height = 10.0
    
    circle_radius = 7.0

    rectangle = Rectangle(rect_width, rect_height)
    
    print(f"Rectangle Area: {rectangle.calculate_area()}")
    
    circle = Circle(circle_radius)
    
    print(f"Circle Area: {circle.calculate_area()}")