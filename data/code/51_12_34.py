class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    sample_side_length = 12
    square_instance = Square(sample_side_length)
    perimeter_result = square_instance.calculate_perimeter()
    print(perimeter_result)