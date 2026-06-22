class Square:
    MIN_SIDE_LENGTH = 0

    @staticmethod
    def compute_area(side_length):
        if side_length < Square.MIN_SIDE_LENGTH:
            raise ValueError("Side length cannot be negative")
        return side_length * side_length

if __name__ == '__main__':
    sample_values = [2.0, 10, 0]
    for value in sample_values:
        try:
            area = Square.compute_area(value)
            print(f"The area of a square with side length {value} is {area}")
        except ValueError as e:
            print(e)