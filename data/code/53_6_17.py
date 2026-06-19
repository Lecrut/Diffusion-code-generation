class Square:
    def __init__(self, side):
        if side < 0:
            raise ValueError("Side length cannot be negative")
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == '__main__':
    square1 = Square(5)
    print(f"Square with side {square1.side} has area {square1.area()}")
    
    square2 = Square(3.5)
    print(f"Square with side {square2.side} has area {square2.area()}")
    
    square3 = Square(0)
    print(f"Square with side {square3.side} has area {square3.area()}")