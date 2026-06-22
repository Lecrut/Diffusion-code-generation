class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    square_properties = {'side_length': 7}
    square = Square(square_properties['side_length'])
    print(square.calculate_area())