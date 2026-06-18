class GeometryCalculator:
    """A class to perform basic geometric calculations."""

    def calculate_area_of_rectangle(self, length: float, width: float) -> float:
        """Calculate the area of a rectangle given its length and width.
        
        Args:
            length (float): The length of the rectangle. Must be non-negative.
            width (float): The width of the rectangle. Must be non-negative.
            
        Returns:
            float: The calculated area as a floating-point number.
            
        Raises:
            ValueError: If either length or width is negative.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative.")
        
        return length * width

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    calc = GeometryCalculator()

    try:
        area_1 = calc.calculate_area_of_rectangle(5.0, 3.0)
        print(f"Area of rectangle with length=5 and width=3 is {area_1}")

        area_2 = calc.calculate_area_of_rectangle(-2.0, 4.0)
    except ValueError as e:
        print(f"Error occurred during calculation: {e}")