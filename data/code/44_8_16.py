class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    sample_length = 12
    sample_width = 7
    rect = Rectangle(sample_length, sample_width)
    print(rect.get_perimeter())