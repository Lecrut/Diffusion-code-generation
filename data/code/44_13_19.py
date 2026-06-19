LENGTH = 8
WIDTH = 6

def calculate_perimeter(length, width):
    return 2 * (length + width)

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)
if __name__ == '__main__':
    perimeter_func = calculate_perimeter(LENGTH, WIDTH)
    print('Perimeter using function:', perimeter_func)
    rectangle = Rectangle(LENGTH, WIDTH)
    perimeter_class = rectangle.perimeter()
    print('Perimeter using class:', perimeter_class)