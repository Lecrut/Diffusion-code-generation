class Square:
    def __init__(self, side_length):
        """Initialize a Square with a given side length."""
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self.side_length = side_length

    def area(self) -> float:
        """Calculate and return the square's area."""
        return self.side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    sample_sides = [5, -3, 0]

    for side in sample_sides:
        try:
            square = Square(side)
            calculated_area = square.area()
            print(f"Square with side {side}: Area is {calculated_area}")
        except ValueError as e:
            print(f"Illegal input 'square': Error -> " + str(e))

    # Example usage of a valid instance created outside the loop.
    large_square = Square(10)
    print("Large square (side 10): Area is", large_square.area())