class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

if __name__ == '__main__':
    rectangle1 = Rectangle(8, 4)
    area_result = rectangle1.calculate_area()
    print(area_result)

    rectangle2 = Rectangle(6, 3)
    area_result = rectangle2.calculate_area()
    print(area_result)