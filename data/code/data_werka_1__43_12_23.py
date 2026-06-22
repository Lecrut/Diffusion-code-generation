class Square:
    def __init__(self, side_length: float):
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        self.side_length = side_length

    def get_area(self) -> float:
        return self.side_length * self.side_length

if __name__ == '__main__':
    try:
        square1 = Square(5)
        area1 = square1.get_area()
        print(f"Area of square 1: {area1}")

        square2 = Square(10.5)
        area2 = square2.get_area()
        print(f"Area of square 2: {area2}")

    except ValueError as e:
        print(e)