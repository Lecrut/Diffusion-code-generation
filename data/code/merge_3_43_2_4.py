class Square:
    def __init__(self, side_length):
        """Initialize a Square with the given side length."""
        if side_length <= 0:
            raise ValueError("Side length must be positive.")
        self.side = float(side_length)

    def calculate_area(self):
        """Calculate and return the area of the square."""
        return self.side ** 2

if __name__ == '__main__':
    side_value = 5.0
    my_square = Square(side_value)
    print(f"Area: {my_square.calculate_area()}")