class Square:
    """A class representing a square with methods to calculate its area."""

    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)) or side_length < 0:
            raise ValueError("Side length must be a non-negative number.")
        
        self._side_length = float(side_length)

    @property
    def area(self):
        """Calculate and return the area of the square."""
        return self._side_length ** 2

if __name__ == '__main__':
    # Create sample Square objects with hard-coded values
    square1 = Square(5.0)
    print(f"Square side: {square1._side_length}, Area: {square1.area}")

    square2 = Square(3)
    print(f"Square side: {square2._side_length}, Area: {square2.area}")