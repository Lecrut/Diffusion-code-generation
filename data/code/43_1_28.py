class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    sample_side_length = 7
    square = Square(sample_side_length)
    area = Square.calculate_area(square.side_length)
    print(area)