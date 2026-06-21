class Square:
    DEFAULT_SIDE_LENGTH = 12

    @staticmethod
    def calculate_perimeter(side_length):
        return 4 * side_length

if __name__ == '__main__':
    sample_side_length = Square.DEFAULT_SIDE_LENGTH
    perimeter = Square.calculate_perimeter(sample_side_length)
    print(perimeter)