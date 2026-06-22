class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_square = Square(7)
    result_area = sample_square.area()
    print(result_area)