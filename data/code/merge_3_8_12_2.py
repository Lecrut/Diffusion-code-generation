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
            ValueError: If either length or width is negative.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative.")
        return length * width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    calc = GeometryCalculator()

    try:
        area = calc.calculate_area_of_rectangle(5, 10)
        print(f"The area of the rectangle is {area}")
        
        # Additional test case with different dimensions
        area2 = calc.calculate_area_of_rectangle(3.5, 4.2)
        print(f"The area of another rectangle is {area2}")
    except ValueError as e:
        print(f"Error occurred: {e}")