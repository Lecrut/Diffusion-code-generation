class Rectangle:
    def __init__(self, length=6, width=4):
        self.length = length
        self.width = width

    def compute_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    my_rectangle = Rectangle()
    perimeter_result = my_rectangle.compute_perimeter()
    print(perimeter_result)