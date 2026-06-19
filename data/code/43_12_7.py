class Square:
    """A class representing a square."""

    def __init__(self, side_length: float) -> None:
        """Initialize the square with a specific side length.

        Args:
            side_length (float): The length of one side of the square. Must be non-negative.

        Raises:
            ValueError: If the side length is negative.
        """
        if side_length < 0:
            raise ValueError("Side length must be non-negative.")
        self.side = side_length

    def area(self) -> float:
        """Calculate and return the area of the square.

        Returns:
            float: The calculated area based on the formula side * side.
        """
        return self.side ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing the Square class
    try:
        sq1 = Square(5)
        print(f"Square with side {sq1.side}: Area is {sq1.area()}")

        sq2 = Square(-3)  # This will trigger a ValueError
    except ValueError as e:
        print(f"Error creating square with negative side: {e}")
    
    try:
        sq3 = Square(0.5)
        print(f"Square with side {sq3.side}: Area is {sq3.area()}")
    except Exception:
        # Handle potential unexpected errors during the sample execution block, though none are expected here.
        pass