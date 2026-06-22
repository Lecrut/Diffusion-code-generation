class Rectangle:
    def __init__(self, length=4, width=2):
        self.length = length
        self.width = width
    
    @staticmethod
    def perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rect = Rectangle(7, 3)
    print(Rectangle.perimeter(rect.length, rect.width))