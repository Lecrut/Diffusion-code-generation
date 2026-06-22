class Square:
    MIN_SIDE_LENGTH = 0

    def __init__(self, side_length):
        if side_length <= self.MIN_SIDE_LENGTH:
            raise ValueError("Side length must be greater than zero")
        self.side_length = side_length

    @staticmethod
    def is_valid_side_length(side_length):
        return isinstance(side_length, (int, float)) and side_length > Square.MIN_SIDE_LENGTH

    def area(self):
        return self._calculate_area()

    def _calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_squares = [
        {'size': 'small', 'length': 3},
        {'size': 'medium', 'length': 5},
        {'size': 'large', 'length': 10}
    ]
    for square_info in sample_squares:
        if Square.is_valid_side_length(square_info['length']):
            square = Square(square_info['length'])
            print(f"The area of a {square_info['size']} square with side length {square_info['length']} is: {square.area()}")
        else:
            print(f"Invalid side length: {square_info['length']}")