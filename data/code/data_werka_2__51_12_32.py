class Square:
    SIDE_LENGTH = 12

    @staticmethod
    def calculate_perimeter(side_length):
        return 4 * side_length
if __name__ == '__main__':
    perimeter = Square.calculate_perimeter(Square.SIDE_LENGTH)
    print(perimeter)