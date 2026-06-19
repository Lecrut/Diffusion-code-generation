class Square:
    def __init__(self, side_length):
        """Initialize a Square object with a given side length."""
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self.side = side_length

    def calculate_area(self) -> float:
        """Calculate and return the area of the square."""
        return self.side * self.side

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no user input required)
    sample_sides = [5, 10.5, -3]

    print("Testing Square class functionality:")
    
    # Test positive integer side length
    square1 = Square(5)
    area1 = square1.calculate_area()
    print(f"Square with side {square1.side}: Area is {area1}")

    # Test float side length
    square2 = Square(10.5)
    area2 = square2.calculate_area()
    print(f"Square with side {square2.side} (float): Area is {area2:.2f}")

    # Demonstrate error handling for negative input without throwing uncaught exception during main logic execution by just showing the setup would fail
    try:
        invalid_square = Square(-3)
    except ValueError as e:
        print(f"Attempting to create a square with side -3 raised an expected error: {e}")

    # Final verification of calculations
    assert area1 == 25, "Area calculation failed for integer input."
    assert abs(area2 - 110.25) < 0.01, "Float precision in area calculation is incorrect."

    print("All basic validations passed.")