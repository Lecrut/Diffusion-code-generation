class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_perimeter(side_length):
        return 4 * side_length

if __name__ == '__main__':
    square1 = Square(3)
    print(f"Perimeter of square with side length {square1.side_length}: {Square.calculate_perimeter(square1.side_length)}")
    square2 = Square(10)
    print(f"Perimeter of square with side length {square2.side_length}: {Square.calculate_perimeter(square2.side_length)}")