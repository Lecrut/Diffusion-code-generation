class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    sample1 = Square(5)
    print(f"Perimeter of square with side {sample1.side_length}: {sample1.calculate_perimeter()}")

    sample2 = Square(8)
    print(f"Perimeter of square with side {sample2.side_length}: {sample2.calculate_perimeter()}")