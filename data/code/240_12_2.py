class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    def calculate_area(self):
        return self.side_length * self.side_length
if __name__ == '__main__':
    side = 5
    my_square = Square(side)
    area = my_square.calculate_area()
    print(area)