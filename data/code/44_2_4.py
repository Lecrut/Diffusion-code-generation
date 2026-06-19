class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

if __name__ == '__main__':
    rect = Rectangle(15, 8)
    perimeter = rect.calculate_perimeter()
    print(perimeter)
    print("Length:", rect.get_length())
    print("Width:", rect.get_width())