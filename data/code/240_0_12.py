class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length = 5
    square_instance = Square(sample_side_length)
    area = square_instance.calculate_area()
    print(f"The side length entered is: {sample_side_length}")
    print(f"The area of the square is: {area}")