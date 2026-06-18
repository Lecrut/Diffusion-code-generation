class GeometryCalculator:
    """A class providing geometric calculations."""

    def calculate_area_of_rectangle(self, length: float, width: float) -> float:
        """Calculate the area of a rectangle given its length and width.

        Args:
            length (float): The length of the rectangle. Must be non-negative.
            width (float): The width of the rectangle. Must be non-negative.

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
    
    # Hard-coded sample values
    sample_length = 5.0
    sample_width = 3.0
    
    area = calculator.calculate_area_of_rectangle(sample_length, sample_width)
    print(f"The area of the rectangle with length {sample_length} and width {sample_width} is: {area}")