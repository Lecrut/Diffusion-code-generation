class Square:

    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length
if __name__ == '__main__':
    sample_values = {'side1': 3, 'side2': 7, 'side3': 9}
    squares = {key: Square(value) for key, value in sample_values.items()}
    for name, square in squares.items():
        print(f'Area of square with side length {square.side_length}: {square.area()}')