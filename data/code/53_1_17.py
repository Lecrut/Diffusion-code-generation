class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_side_length = 7
    square_instance = Square(sample_side_length)
    print(square_instance.area())