class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    sample_length = 8.0
    sample_width = 4.5
    rectangle = Rectangle(sample_length, sample_width)
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())