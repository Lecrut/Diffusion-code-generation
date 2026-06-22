class SquareProperties:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def compute_side_length(self):
        return self.area ** 0.5

    def compute_perimeter(self):
        side_length = self.compute_side_length()
        return 4 * side_length

if __name__ == '__main__':
    square_area = 16
    try:
        square = SquareProperties(square_area)
        side_length = square.compute_side_length()
        perimeter = square.compute_perimeter()
        print(f"Side Length: {side_length}, Perimeter: {perimeter}")
    except ValueError as e:
        print(e)