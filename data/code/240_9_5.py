class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    square_instance = Square(3)
    area = square_instance.calculate_area()
    print(area)