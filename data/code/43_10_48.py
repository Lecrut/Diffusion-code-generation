class Square:
    MIN_SIDE_LENGTH = 0

    @staticmethod
    def calculate_square_area(side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number")
        if side_length < Square.MIN_SIDE_LENGTH:
            raise ValueError("Side length cannot be negative")
        return side_length * side_length

if __name__ == '__main__':
    sample_values = [4.0, 12, -3, 'b']
    for value in sample_values:
        try:
            print(Square.calculate_square_area(value))
        except (TypeError, ValueError) as e:
            print(f"Error with value {value}: {e}")