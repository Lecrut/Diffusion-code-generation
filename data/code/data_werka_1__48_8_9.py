class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

if __name__ == '__main__':
    rect1 = Rectangle(5.5, 3.2)
    area1 = rect1.calculate_area()
    print(area1)

    rect2 = Rectangle(7.8, 4.1)
    area2 = rect2.calculate_area()
    print(area2)