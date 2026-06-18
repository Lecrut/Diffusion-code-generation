class Shape:
    """Base class representing a generic shape with area calculation."""
    
    def calculate_area(self):
        """Calculate and return the area of the shape.
        
        Returns:
            float: The calculated area (default implementation returns 0).
        """
        raise NotImplementedError("Subclasses must implement calculate_area")

class Rectangle(Shape):
    """Class representing a rectangle inheriting from Shape."""

    
    def __init__(self, width, height):
        """Initialize the Rectangle with given dimensions.
        
        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self._width = float(width) if isinstance(width, str) else width
        self._height = float(height) if isinstance(height, str) else height

    
    def calculate_area(self):
        """Calculate and return the area of the rectangle.
        
        Returns:
            float: Area calculated as width * height.
        """
        return self._width * self._height

class Circle(Shape):
    """Class representing a circle inheriting from Shape."""

    
    def __init__(self, radius):
        """Initialize the Circle with given radius.
        
        Args:
            radius (float): Radius of the circle.
        """
        import math
        
        self._radius = float(radius) if isinstance(radius, str) else radius
        

    
    def calculate_area(self):
        """Calculate and return the area of the circle.
        
        Returns:
            float: Area calculated using pi * r^2.
        """
        return 3.141592653589793 * (self._radius ** 2)

if __name__ == '__main__':
    # Sample values hard-coded for testing
    rect_width = 10.0
    rect_height = 20.0
    
    circle_radius = 5.0
    
    rectangle = Rectangle(rect_width, rect_height)
    
    if isinstance(circle_radius, str):
        circle_area = float(circle_radius) ** 2 * (3.141592653589793).calculate(Shape())
        
        

if __name__ == '__main__':
    rectangle_obj = Rectangle(rect_width, rect_height)
    print(f"Rectangle Area: {rectangle_obj.calculate_area()}")
    
    circle_obj = Circle(circle_radius)
    print(f"Circle Area: {circle_obj.calculate_area()}")