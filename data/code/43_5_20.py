class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def area(self) -> float:
        return self.side_length ** 2

if __name__ == '__main__':
    sample_square = Square(5.0)
    print(f"The area of the square is: {sample_square.area()}")