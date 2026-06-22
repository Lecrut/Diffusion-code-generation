class Square:
    MIN_SIDE_LENGTH = 1

    @staticmethod
    def calculate_area(side_length):
        if side_length < Square.MIN_SIDE_LENGTH:
            raise ValueError("Side length must be at least 1")
        return side_length * side_length

if __name__ == '__main__':
    try:
        sample_side_length = 6
        area = Square.calculate_area(sample_side_length)
        print(area)
    except ValueError as e:
        print(e)