class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_values = {
        'small_square': 3,
        'medium_square': 7.5,
        'large_square': 10
    }

    for name, side in sample_values.items():
        square = Square(side)
        print(f"The area of the {name} square is: {square.area()}")