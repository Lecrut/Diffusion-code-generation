class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print("Length:", rect.length)
    print("Width:", rect.width)
    print("Area:", rect.area())