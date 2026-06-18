class Square:
    """A class representing a square with its side length."""

    def __init__(self, side_length):
        """Initialize the Square object with a valid non-negative side length.

        Args:
            side_length (float or int): The length of one side of the square.
                Must be greater than zero to form a valid geometric figure.
        Raises:
            ValueError: If the provided side length is not positive.
        """
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")

        self._side = float(side_length)

    @property
    def area(self):
        """Calculate and return the area of the square."""
        return self._side ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access.
    try:
        side_a = 5.0
        square_1 = Square(side_a)
        area_a = square_1.area

        side_b = 3
        square_2 = Square(side_b)
        area_b = square_2.area

        print(f"Square with side {side_a}: Area is {area_a}")
        print(f"Square with side {side_b} (int): Area is {area_b}")
    except ValueError as e:
        # Demonstrating error handling, though sample values should not trigger this.
        print(f"Error creating square: {e}")