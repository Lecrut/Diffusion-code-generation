class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    try:
        sample_side_lengths = [2, 3, 4]
        for side in sample_side_lengths:
            square = Square(side)
            area = square.calculate_area()
            print(f"The area of the square with side length {side} is: {area}")
    except ValueError as e:
        print(e)