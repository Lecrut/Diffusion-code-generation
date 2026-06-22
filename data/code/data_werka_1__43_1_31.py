class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self._calculate_area()

    def _calculate_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    example_side = 7
    square_instance = Square(example_side)
    print(square_instance.area())