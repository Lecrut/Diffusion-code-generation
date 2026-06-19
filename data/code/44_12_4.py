class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect = Rectangle(15, 7)
    print("Length:", rect.get_length())
    print("Width:", rect.get_width())
    print("Perimeter:", rect.calculate_perimeter())