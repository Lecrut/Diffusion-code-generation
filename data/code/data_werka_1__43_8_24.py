class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    square1 = Square(3)
    print(f"The side length of square1 is: {square1.side_length}")
    print(f"The area of square1 is: {square1.area()}")

    square2 = Square(7)
    print(f"The side length of square2 is: {square2.side_length}")
    print(f"The area of square2 is: {square2.area()}")