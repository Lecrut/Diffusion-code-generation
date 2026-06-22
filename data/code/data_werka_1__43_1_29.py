SQUARE_SIDE_LENGTH = 5

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    square_instance = Square(SQUARE_SIDE_LENGTH)
    print(square_instance.area())