class Square:

    def __init__(self, side_length: float):
        self.side_length = side_length

    def get_area(self) -> float:
        return self.side_length * self.side_length
if __name__ == '__main__':
    square1 = Square(3.0)
    area1 = square1.get_area()
    print(f'Area of square 1 with side length {square1.side_length}: {area1}')
    square2 = Square(7.5)
    area2 = square2.get_area()
    print(f'Area of square 2 with side length {square2.side_length}: {area2}')