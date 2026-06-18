class Square:
    def __init__(self, side_length):
        """Initialize a Square with the given side length."""
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self._side = float(side_length)

    @property
    def area(self):
        """Calculate and return the area of the square."""
        return self._side ** 2

if __name__ == '__main__':
    side_a = 5.0
    side_b = 10
    
    square_1 = Square(side_a)
    print(f"Square with side {side_a}: Area is {square_1.area}")

    square_2 = Square(side_b)
    print(f"Square with side {side_b}: Area is {square_2.area}")