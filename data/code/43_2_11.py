class Square:
    """A class representing a square with methods to calculate its area."""

    def __init__(self, side_length):
        """Initialize the Square object with the given side length.

        Args:
            side_length (float or int): The length of one side of the square. Must be non-negative.
        Raises:
            ValueError: If side_length is negative.
        """
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self._side = float(side_length)

    @property
    def area(self):
        """Calculate and return the area of the square."""
        return self._side ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access.
    side = 5.0

    try:
        square = Square(side)
        calculated_area = square.area
        print(f"Square with side length {side} has an area of {calculated_area}")
    except ValueError as e:
        print(f"Error creating Square object: {e}")