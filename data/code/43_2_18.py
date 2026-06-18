class Square:
    """A class representing a square with methods to calculate its area."""
    
    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)) or side_length < 0:
            raise ValueError("Side length must be a non-negative number.")
        self.side = side_length
    
    def get_area(self) -> float:
        """Calculate and return the area of the square."""
        return self.side * self.side

if __name__ == '__main__':
    # Sample values for testing
    sample_sides = [5, 0.5, -3]

    print("Testing Square class:\n")

    try:
        sq1 = Square(5)
        area1 = sq1.get_area()
        print(f"Square with side {sq1.side} has an area of: {area1}")

        sq2 = Square(0.5)
        area2 = sq2.get_area()
        print(f"Square with side {sq2.side} has an area of: {area2}")

    except ValueError as e:
        print(f"Error creating square: {e}")