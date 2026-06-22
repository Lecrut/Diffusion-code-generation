class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side * self.side

if __name__ == '__main__':
    square1 = Square(4)
    print(f"The area of the first square is: {square1.area}")
    
    square2 = Square(6)
    print(f"The area of the second square is: {square2.area}")

    square3 = Square(8)
    print(f"The area of the third square is: {square3.area}")