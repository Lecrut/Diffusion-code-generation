class GeometryCalculator:
    """A class to perform basic geometric calculations."""

    def calculate_area_of_rectangle(self, length: float, width: float) -> float:
        """
        Calculates the area of a rectangle given its length and width.

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
    # Hard-coded sample values for testing the GeometryCalculator class
    calculator = GeometryCalculator()

    try:
        area = calculator.calculate_area_of_rectangle(5, 10)
        print(f"The area of a rectangle with dimensions {5} and {10} is {area}")
        
        # Additional test case to demonstrate negative validation behavior without throwing an error in the main output block above
        try:
            invalid_area = calculator.calculate_area_of_rectangle(-3, 4)
        except ValueError as e:
            print(f"Caught expected error for negative dimension: {e}")
            
    except Exception as ex:
        # This handles any unexpected runtime errors during execution
        print(f"An unexpected error occurred: {ex}")