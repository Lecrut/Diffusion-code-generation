class Square:
    MIN_SIDE_LENGTH = 0

    @staticmethod
    def is_valid_side_length(side_length):
        return isinstance(side_length, (int, float)) and side_length >= Square.MIN_SIDE_LENGTH

    @staticmethod
    def calculate_area(side_length):
        if not Square.is_valid_side_length(side_length):
            raise ValueError('Side length must be a non-negative numeric value.')
        return side_length * side_length

if __name__ == '__main__':
    sample_values = [5, 3.5, -2, 'a']
    for value in sample_values:
        try:
            area = Square.calculate_area(value)
            print(f"Area of square with side {value}: {area}")
        except ValueError as e:
            print(e)