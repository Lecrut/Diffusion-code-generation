class Square:
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length must be positive")
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == '__main__':
    sample_sides = [5, 3, 7, 10]
    for side in sample_sides:
        try:
            square = Square(side)
            print(f"The area of the square with side {side} is: {square.area()}")
        except ValueError as e:
            print(e)