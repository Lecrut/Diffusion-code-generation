class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_values = [3, 0, 4.5]
    for value in sample_values:
        square = Square(value)
        print(f"The area of a square with side length {value} is {square.area()}")