class Square:
    MIN_SIDE_LENGTH = 1
    
    def __init__(self, side_length):
        self._validate_side_length(side_length)
        self.side_length = side_length
    
    @staticmethod
    def _validate_side_length(side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number")
        if side_length < Square.MIN_SIDE_LENGTH:
            raise ValueError(f"Side length must be at least {Square.MIN_SIDE_LENGTH}")
    
    def area(self):
        return self._calculate_area()
    
    @staticmethod
    def _calculate_area(side_length):
        return side_length ** 2

if __name__ == '__main__':
    sample_side_lengths = [3, 5.5, 10]
    for length in sample_side_lengths:
        try:
            square = Square(length)
            print(f"The area of a square with side length {length} is: {square.area()}")
        except (ValueError, TypeError) as e:
            print(e)