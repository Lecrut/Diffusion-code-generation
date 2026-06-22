class Rectangle:
    def __init__(self, length=4, width=2):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect = Rectangle(7, 3)
    perimeter_result = rect.calculate_perimeter()
    print(perimeter_result)