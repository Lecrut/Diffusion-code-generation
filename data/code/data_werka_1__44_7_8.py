class Rectangle:
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError("Length must be a positive number.")
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self._width = value

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        sample_length = '7'
        sample_width = '3'
        rectangle = Rectangle(sample_length, sample_width)
        perimeter = rectangle.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)