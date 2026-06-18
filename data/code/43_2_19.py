class Square:
    def __init__(self, side_length):
        """Initialize a Square with a given side length."""
        self.side_length = float(side_length)

    @property
    def area(self):
        """Calculate and return the area of the square."""
        return self.side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate usage without user input
    side_1 = Square(5.0)
    print(f"Square with side {side_1.side_length} has an area of: {side_1.area}")

    square_2 = Square("7")  # Allow string conversion during initialization logic implicitly handled by float()
    
    assert abs(square_2.area - 49.0) < 0.01, "Area calculation failed"
    print(f"Square with side {square_2.side_length} has an area of: {square_2.area}")

    # Test edge case with zero
    square_zero = Square(0)
    assert square_zero.area == 0.0
    print("Zero-area test passed.")