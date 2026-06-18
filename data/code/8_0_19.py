import math

class Rectangle:
    """A class to represent a rectangle with properties area calculation."""

    def __init__(self, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Width and height must be numeric.")
        self.width = width
        self.height = height
        # Calculate area in the constructor for immediate use
        _calculate_area(self)

    @staticmethod
    def calculate_dimension(dimension_name):
        """Validates that a dimension is positive."""
        if not isinstance(dimension, (int, float)):
            raise TypeError(f"Dimension '{dimension_name}' must be numeric.")

def _calculate_area(rectangle: Rectangle) -> None:
    """Private method to compute and set the area of the rectangle.

    Args:
        rectangle (Rectangle): The instance whose area is being calculated.

    Returns:
        None
    """

if __name__ == '__main__':
    pass
