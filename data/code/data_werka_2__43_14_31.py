class Square:
    MIN_SIDE_LENGTH = 0
    
    def __init__(self, side_length):
        self.side_length = side_length
    
    def is_valid_side_length(self):
        return isinstance(self.side_length, (int, float)) and self.side_length >= self.MIN_SIDE_LENGTH
    
    def calculate_area(self):
        if not self.is_valid_side_length():
            raise ValueError('Side length must be a non-negative numeric value.')
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_values = [5, 3.5, -2, 'a']
    for value in sample_values:
        try:
            square = Square(value)
            area = square.calculate_area()
            print(f"Area of square with side {value}: {area}")
        except ValueError as e:
            print(e)