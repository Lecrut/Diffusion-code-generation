class Square:
    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def get_area(self) -> float:
        return self.side_length ** 2

if __name__ == '__main__':
    try:
        square1 = Square(7.5)
        print(f"Area of square 1: {square1.get_area()}")
        
        square2 = Square(3.0)
        print(f"Area of square 2: {square2.get_area()}")
    except ValueError as e:
        print(e)