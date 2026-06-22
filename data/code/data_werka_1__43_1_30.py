class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    side_size = 7
    square_instance = Square(side_size)
    area_result = square_instance.calculate_area()
    print(area_result)