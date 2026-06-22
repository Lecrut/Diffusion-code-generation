class Square:
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length must be positive")
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == '__main__':
    try:
        square1 = Square(5)
        print(f"The area of the first square is: {square1.area()}")
        
        square2 = Square(3)
        print(f"The area of the second square is: {square2.area()}")
        
        square3 = Square(7)
        print(f"The area of the third square is: {square3.area()}")
    except ValueError as e:
        print(e)