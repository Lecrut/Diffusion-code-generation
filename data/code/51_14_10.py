class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

if __name__ == '__main__':
    square_config = {'side': 8}
    square = Square(square_config['side'])
    print(square.perimeter())