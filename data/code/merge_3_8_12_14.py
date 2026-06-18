class GeometryCalculator:
    """A class to perform basic geometric calculations."""

    def calculate_area_of_rectangle(self, length: float, width: float) -> float:
        """
        Calculate the area of a rectangle given its length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.

        Returns:
            float: The calculated area of the rectangle.
        
        Raises:
            ValueError: If either dimension is negative.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative.")
        return length * width

if __name__ == '__main__':
    calculator = GeometryCalculator()
    
    # Hard-coded sample values for testing without user input
    sample_length = 5.0
    sample_width = 3.0
    
    area = calculator.calculate_area_of_rectangle(sample_length, sample_width)
    print(f"The area of the rectangle is: {area}")