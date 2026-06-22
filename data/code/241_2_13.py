class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def compute_area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect1 = Rectangle(10, 5)
    print("Area of rectangle 1:", rect1.compute_area())
    
    rect2 = Rectangle(7, 3)
    print("Area of rectangle 2:", rect2.compute_area())