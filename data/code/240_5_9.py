class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == '__main__':
    square = Square(4)
    print(f"Side: {square.side}, Area: {square.area()}")