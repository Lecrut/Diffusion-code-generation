class Square:
    def __init__(self, side):
        if side < 0:
            raise ValueError("Side length cannot be negative")
        self.side = side

    @staticmethod
    def area(side):
        return side * side

if __name__ == '__main__':
    sample_sides = [3, 5, 7]
    for side in sample_sides:
        square = Square(side)
        print(f"Side Length: {side}, Area: {Square.area(square.side)}")