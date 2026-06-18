class Square:
    """A class representing a square."""

    def __init__(self, side_length):
        """Initialize the Square with the given side length.

        Args:
            side_length (float or int): The length of the sides of the square. Must be non-negative.
        Raises:
            ValueError: If side_length is negative.
        """
        if not isinstance(side_length, (int, float)):
            raise TypeError("side_length must be a number")
        if side_length < 0:
            raise ValueError("side_length cannot be negative")

        self._side = side_length

    def area(self) -> float:
        """Calculate and return the area of the square.

        Returns:
            float: The area calculated as side_length squared.
        """
        return self._side ** 2

if __name__ == '__main__':
    # Sample usage without user input
    try:
        sample_square = Square(5)
        print(f"Square with side length {sample_square._side}")
        print(f"Area: {sample_square.area()}")

        sample_square_2 = Square(0.75)
        print(f"\nSquare with side length {sample_square_2._side}")
        print(f"Area: {sample_square_2.area()}")
    except (TypeError, ValueError) as e:
        print(f"Error creating square: {e}")