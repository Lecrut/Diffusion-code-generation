class GeometryCalculator:
    """A class providing geometric calculation utilities."""

    def calculate_area_of_rectangle(self, length: float, width: float) -> float:
        """
        Calculates the area of a rectangle given its length and width.

        Args:
            length (float): The length of the rectangle in units. Must be non-negative.
            width (float): The width of the rectangle in units. Must be non-negative.

        Returns:
            float: The calculated area of the rectangle. Raises ValueError if dimensions are negative.
        
        Raises:
            ValueError: If either length or width is less than zero.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative values.")
        
        return length * width

if __name__ == '__main__':
    # Sample usage with hard-coded values; no user input required.
    calculator = GeometryCalculator()

    sample_length = 10.5
    sample_width = 6.2
    
    area = calculator.calculate_area_of_rectangle(sample_length, sample_width)
    
    print(f"Rectangle Dimensions: {sample_length} x {sample_width}")
    print(f"Calculated Area: {area:.2f}")

    # Additional test case for negative input validation demonstration (optional run logic omitted as it would raise error in silent mode, so just demonstrating the call that works)
    
    area_square = calculator.calculate_area_of_rectangle(5.0, 5.0)
    print(f"Square Area: {area_square}")