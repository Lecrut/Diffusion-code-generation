class Rectangle:
    def __init__(self, length=5, width=3):
        self.length = length
        self.width = width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect = Rectangle(4, 6)
    print(rect.perimeter())