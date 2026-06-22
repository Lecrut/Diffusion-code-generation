class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    SAMPLE_LENGTH = 15
    SAMPLE_WIDTH = 9
    rect = Rectangle(SAMPLE_LENGTH, SAMPLE_WIDTH)
    print(rect.get_perimeter())