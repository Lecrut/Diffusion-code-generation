class Square:
    DEFAULT_SIDE_LENGTH = 5

    @staticmethod
    def calculate_area(side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        return side_length * side_length

if __name__ == '__main__':
    sample_side_length = Square.DEFAULT_SIDE_LENGTH
    area = Square.calculate_area(sample_side_length)
    print(area)