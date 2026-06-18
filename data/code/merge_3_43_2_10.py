class Square:
    def __init__(self, side_length):
        """Initialize a Square object with a given side length."""
        self.side_length = side_length
    
    @property
    def area(self) -> float:
        """Calculate and return the area of the square."""
        if self.side_length < 0:
            raise ValueError("Side length cannot be negative.")
        return self.side_length ** 2

if __name__ == '__main__':
    side = 5.0
    my_square = Square(side)
    print(f"The area of a square with side {side} is {my_square.area}")