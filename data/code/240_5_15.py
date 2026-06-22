class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == '__main__':
    square_instance = Square(4)
    print(f"Side: {square_instance.side}, Area: {square_instance.area()}")