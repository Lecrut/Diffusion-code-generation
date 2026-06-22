class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    square_instance = Square(5.0)
    area_result = square_instance.calculate_area()
    print(f"The side length of the square is: {square_instance.side_length}")
    print(f"The area of the square is: {area_result}")