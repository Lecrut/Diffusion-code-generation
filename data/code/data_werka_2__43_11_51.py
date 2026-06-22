class Square:
    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def get_area(self) -> float:
        return self.side_length ** 2

if __name__ == '__main__':
    square = Square(5.0)
    print(square.get_area())