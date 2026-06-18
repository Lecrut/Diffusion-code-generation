class Shape:
    """Base class representing a geometric shape with an area calculation method."""
    
    def calculate_area(self):
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement the 'calculate_area' method.")

class Rectangle(Shape):
    """Class representing a rectangle that calculates its area."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    """Class representing a circle that calculates its area."""

    PI_VALUE = 3.141592653589793
    
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return Circle.PI_VALUE * (self.radius ** 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    rect_width = 5.0
    rect_height = 3.0
    
    circle_radius = 7.0

    rectangle = Rectangle(rect_width, rect_height)
    area_rectangle = rectangle.calculate_area()

    circle = Circle(circle_radius)
    area_circle = circle.calculate_area()

    print(f"Rectangle Area: {area_rectangle}")
    print(f"Circle Area: {area_circle}")