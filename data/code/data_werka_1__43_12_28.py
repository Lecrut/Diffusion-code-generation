class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def get_area(self) -> float:
        return self.side_length * self.side_length

if __name__ == '__main__':
    square_dimensions = {
        'square1': 5,
        'square2': 10.5
    }

    for name, side in square_dimensions.items():
        square = Square(side)
        area = square.get_area()
        print(f"Area of {name}: {area}")