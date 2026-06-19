class Square:
    def __init__(self, side_length):
        """Initialize a Square object with the given side length."""
        self.side = side_length

    def calculate_area(self) -> float:
        """Calculate and return the area of the square.

        Returns:
            The area as a float or integer if input is exact.
        """
        return self.side ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    side1 = 5
    side2 = 3.5

    square_1 = Square(side1)
    area_1 = square_1.calculate_area()
    print(f"Area of square with side {side1}: {area_1}")

    square_2 = Square(side2)
    area_2 = square_2.calculate_area()
    print(f"Area of square with side {side2}: {area_2}")