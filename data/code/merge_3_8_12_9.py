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
    # Sample values for testing the calculate_area_of_rectangle method
    calc = GeometryCalculator()

    try:
        area = calc.calculate_area_of_rectangle(5.0, 10.0)
        print(f"The area of a rectangle with length 5.0 and width 10.0 is {area}.")
        
        # Additional test case
        area2 = calc.calculate_area_of_rectangle(-3.0, 4.0)
    except ValueError as ve:
        print(f"Error occurred: {ve}")