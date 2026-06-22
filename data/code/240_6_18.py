class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == '__main__':
    square_instance = Square(5.0)
    print(f"The side length of the square is: {square_instance.side}")
    print(f"The area of the square is: {square_instance.area()}")