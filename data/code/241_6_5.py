class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    area = rect.calculate_area()
    print(area)