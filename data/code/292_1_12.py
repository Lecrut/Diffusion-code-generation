class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @staticmethod
    def calculate_perimeter(side_length):
        return 4 * side_length

if __name__ == '__main__':
    sample_side1 = 3
    square1 = Square(sample_side1)
    perimeter1 = square1.calculate_perimeter(sample_side1)
    print(f"Perimeter for side length {sample_side1}: {perimeter1}")

    sample_side2 = 10
    square2 = Square(sample_side2)
    perimeter2 = square2.calculate_perimeter(sample_side2)
    print(f"Perimeter for side length {sample_side2}: {perimeter2}")