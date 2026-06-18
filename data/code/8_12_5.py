class GeometryCalculator:
    """A class to perform basic geometric calculations."""

    def calculate_area_of_rectangle(self, length: float, width: float) -> float:
        """
        Calculates the area of a rectangle given its length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.

        Returns:
            float: The calculated area of the rectangle.
        """
        return length * width

if __name__ == '__main__':
    calculator = GeometryCalculator()
    
    # Hard-coded sample values
    sample_length = 5.0
    sample_width = 3.0
    
    result = calculator.calculate_area_of_rectangle(sample_length, sample_width)
    print(f"The area of the rectangle with length {sample_length} and width {sample_width} is: {result}")