class Square:
    def __init__(self, side_length: float):
        if not isinstance(side_length, (int, float)) or side_length < 0:
            raise ValueError("Side length must be a non-negative number")
        self.side_length = side_length

    def area(self) -> float:
        return float(self.side_length ** 2)

if __name__ == '__main__':
    square1 = Square(5.0)
    print(f"The area of the square with side length {square1.side_length} is {square1.area()}")

    square2 = Square(10.5)
    print(f"The area of the square with side length {square2.side_length} is {square2.area()}")