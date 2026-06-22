class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def compute_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_values = [2.5, 6, -3]
    for value in sample_values:
        try:
            square = Square(value)
            area = square.compute_area()
            print(f"The area of a square with side length {value} is {area}")
        except ValueError as e:
            print(e)