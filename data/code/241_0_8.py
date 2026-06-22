class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    area = rect.calculate_area()
    print(area)