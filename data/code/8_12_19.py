class GeometryCalculator:
    """A class to perform basic geometric calculations."""

    def calculate_area_of_rectangle(self, length: float, width: float) -> float:
        """Calculates the area of a rectangle given its length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.

        Returns:
            float: The calculated area of the rectangle.
        
        Raises:
            ValueError: If either length or width is negative.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative.")
        return length * width

if __name__ == '__main__':
    # Sample usage with hard-coded values
    calculator = GeometryCalculator()
    
    length = 5.0
    width = 3.0
    
    area = calculator.calculate_area_of_rectangle(length, width)
    print(f"The area of the rectangle is: {area}")