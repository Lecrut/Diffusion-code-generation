class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def area(self) -> int:
        return self.length * self.width

if __name__ == '__main__':
    rect1 = Rectangle(5, 4)
    print(f"Area of rectangle with length 5 and width 4: {rect1.area()}")
    
    rect2 = Rectangle(3, 7)
    print(f"Area of rectangle with length 3 and width 7: {rect2.area()}")
    
    rect3 = Rectangle(8, 9)
    print(f"Area of rectangle with length 8 and width 9: {rect3.area()}")