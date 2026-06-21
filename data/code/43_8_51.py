class Square:
    def __init__(self, side):
        self.side = side

    @staticmethod
    def calculate_area(side):
        return side ** 2

if __name__ == '__main__':
    sample_side = 7
    square = Square(sample_side)
    print(Square.calculate_area(square.side))