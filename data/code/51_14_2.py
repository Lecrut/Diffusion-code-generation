class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    square_properties = {'side_length': 7}
    square = Square(square_properties['side_length'])
    print(square.perimeter())