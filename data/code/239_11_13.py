class Rectangle:
    def __init__(self, length=4, width=2):
        if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
            raise ValueError("Length and width must be numbers.")
        self.length = length
        self.width = width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect = Rectangle(7, 3)
    print(rect.perimeter())