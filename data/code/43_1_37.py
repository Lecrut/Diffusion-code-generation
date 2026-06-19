class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    config = {'side': 5}
    square_instance = Square(config['side'])
    print(square_instance.area())