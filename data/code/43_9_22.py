class Square:
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length must be positive")
        self.side = side

    def area(self):
        return self.side ** 2

if __name__ == '__main__':
    try:
        sample_side = 5
        square = Square(sample_side)
        print(f"The area of a square with side length {sample_side} is {square.area()}")
    except ValueError as e:
        print(e)