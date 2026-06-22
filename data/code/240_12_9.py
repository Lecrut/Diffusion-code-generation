class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    square1 = Square(5)
    area1 = Square.calculate_area(square1.side_length)
    print(f"Area of square 1: {area1}")
    square2 = Square(10.5)
    area2 = Square.calculate_area(square2.side_length)
    print(f"Area of square 2: {area2}")