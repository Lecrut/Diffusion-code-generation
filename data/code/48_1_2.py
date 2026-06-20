class Shape:
    def __init__(self):
        self.values = {}

    def set_square(self, side):
        self.values['square_side'] = side

    def set_rectangle(self, length, width):
        self.values['rect_length'] = length
        self.values['rect_width'] = width

    def get_square_perimeter(self):
        side = self.values.get('square_side')
        return side * 4

    def get_square_area(self):
        side = self.values.get('square_side')
        return side ** 2

    def get_rectangle_perimeter(self):
        length = self.values.get('rect_length')
        width = self.values.get('rect_width')
        return 2 * (length + width)

    def get_rectangle_area(self):
        length = self.values.get('rect_length')
        width = self.values.get('rect_width')
        return length * width

if __name__ == '__main__':
    shape = Shape()
    shape.set_square(7)
    print(shape.get_square_perimeter())
    print(shape.get_square_area())
    shape.set_rectangle(10, 4)
    print(shape.get_rectangle_perimeter())
    print(shape.get_rectangle_area())