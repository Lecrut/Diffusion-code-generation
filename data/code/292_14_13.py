class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    square1 = Square(5)
    print(f"Perimeter of square with side length {square1.side_length}: {square1.calculate_perimeter()}")

    square2 = Square(7)
    print(f"Perimeter of square with side length {square2.side_length}: {square2.calculate_perimeter()}")