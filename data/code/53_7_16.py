class Square:

    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length
if __name__ == '__main__':
    square_instance = Square(7.5)
    calculated_area = square_instance.area()
    print(f'The area of the square is: {calculated_area}')