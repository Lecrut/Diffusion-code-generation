class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    square1 = Square(5)
    print(f"Side Length: {square1.side_length}, Area: {square1.area()}")

    square2 = Square(7.2)
    print(f"Side Length: {square2.side_length}, Area: {square2.area()}")