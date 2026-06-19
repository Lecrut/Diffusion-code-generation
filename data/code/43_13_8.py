class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def get_side_length(self):
        return self.side_length

if __name__ == '__main__':
    sample_squares = [Square(3), Square(4), Square(5)]
    for square in sample_squares:
        print(f"Side Length: {square.get_side_length()}, Area: {square.calculate_area()}")