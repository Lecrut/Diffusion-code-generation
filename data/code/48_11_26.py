class SquareMetrics:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def calculate_side_length(self):
        return self.area ** 0.5

    def calculate_perimeter(self):
        side_length = self.calculate_side_length()
        return 4 * side_length

if __name__ == '__main__':
    try:
        square_area = 16
        square_metrics = SquareMetrics(square_area)
        side_length = square_metrics.calculate_side_length()
        perimeter = square_metrics.calculate_perimeter()
        print(f"Side Length: {side_length}, Perimeter: {perimeter}")
    except ValueError as e:
        print(e)