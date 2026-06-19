class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    SAMPLE_SIDE_LENGTH = 7
    square_instance = Square(SAMPLE_SIDE_LENGTH)
    computed_area = square_instance.area()
    print(computed_area)