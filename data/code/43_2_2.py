class Square:
    """A class representing a square with methods to calculate its area."""

    def __init__(self, side_length):
        """Initialize the Square object with a valid non-negative side length.

        Args:
            side_length (float or int): The length of one side of the square. Must be >= 0.
        
        Raises:
            ValueError: If the provided side_length is negative.
        """
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self.side = float(side_length)

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            float: The calculated area (side * side).
        """
        return self.side ** 2

if __name__ == '__main__':
    # Sample values to demonstrate functionality without user input or external dependencies
    sample_sides = [5, -3, 0.0]

    for s in sample_sides:
        try:
            square = Square(s)
            calculated_area = square.area()
            print(f"Square with side {s} has an area of {calculated_area}")
        except ValueError as e:
            print(f"Error creating square with side {s}: {e}")