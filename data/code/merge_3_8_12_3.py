class GeometryCalculator:
    """A class providing geometric calculations."""

    def calculate_area_of_rectangle(self, length: float, width: float) -> float:
        """Calculates the area of a rectangle given its length and width.

        Args:
            length (float): The length of the rectangle. Must be non-negative.
            width (float): The width of the rectangle. Must be non-negative.

        Returns:
            float: The calculated area of the rectangle. Raises ValueError if inputs are negative.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative.")
        
        return length * width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    calc = GeometryCalculator()

    try:
        area = calc.calculate_area_of_rectangle(5, 10)
        print(f"The area of the rectangle with length {5} and width {10} is {area}.")
        
        # Additional test case
        area2 = calc.calculate_area_of_rectangle(-3.5, 4.0)
    except ValueError as e:
        print(f"Error occurred during calculation: {e}")