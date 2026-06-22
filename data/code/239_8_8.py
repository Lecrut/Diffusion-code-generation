class Rectangle:
    def __init__(self, width=5, height=3):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect1 = Rectangle()
    print("Perimeter of default rectangle:", rect1.calculate_perimeter())
    
    rect2 = Rectangle(10, 6)
    print("Perimeter of rectangle with width=10, height=6:", rect2.calculate_perimeter())