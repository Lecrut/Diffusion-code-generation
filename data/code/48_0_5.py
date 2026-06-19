class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

if __name__ == '__main__':
    rect1 = Rectangle(5, 10)
    print(rect1.calculate_area())
    
    rect2 = Rectangle(7, 3)
    print(rect2.calculate_area())