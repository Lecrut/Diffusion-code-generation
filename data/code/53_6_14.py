class Square:
    def __init__(self, side):
        self.side = side

    @staticmethod
    def calculate_area(side):
        return side * side

if __name__ == '__main__':
    sample_sides = [3, 5, 7, 10]
    for side in sample_sides:
        square = Square(side)
        area = Square.calculate_area(square.side)
        print(f"Side Length: {side}, Area: {area}")