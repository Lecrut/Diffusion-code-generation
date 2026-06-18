class Square:
    """A class representing a square with methods to calculate its area."""

    def __init__(self, side_length):
        """Initialize the Square object with a given side length.

        Args:
            side_length (float or int): The length of one side of the square.
                                      Must be non-negative.
        Raises:
            ValueError: If side_length is negative.
        """
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self._side = side_length

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            float or int: The calculated area (side * side).
        """
        return self._side ** 2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_sides = [5, 3.5, -1]

    for s in sample_sides:
        try:
            square = Square(s)
            print(f"Square side: {s}, Area: {square.area()}")
        except ValueError as e:
            print(f"Error creating Square with side {s}: {e}")