class Square:

    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)) or side_length < 0:
            raise ValueError('Side length must be a non-negative number')
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2
if __name__ == '__main__':
    try:
        side_length_value = 8.2
        sample_square = Square(side_length_value)
        area_result = sample_square.get_area()
        print(f'The area of the square with side {side_length_value} is: {area_result}')
    except ValueError as e:
        print(e)