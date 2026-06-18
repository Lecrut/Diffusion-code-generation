class GeometryCalculator:
    """A class providing geometric calculation utilities."""

    def calculate_area_of_rectangle(self, length: float, width: float) -> float:
        """
        Calculate the area of a rectangle given its length and width.

        Args:
            length (float): The length of the rectangle. Must be non-negative.
            width (float): The width of the rectangle. Must be non-negative.

        Returns:
            float: The calculated area of the rectangle.

        Raises:
            ValueError: If either dimension is negative.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative numbers.")
        
        return length * width

if __name__ == '__main__':
    # Sample execution with hard-coded values
    calculator = GeometryCalculator()
    
    sample_length = 10.5
    sample_width = 4.2
    
    area_result = calculator.calculate_area_of_rectangle(sample_length, sample_width)
    
    print(f"Rectangle Area: {area_result}")