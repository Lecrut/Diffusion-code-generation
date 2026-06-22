class Square:
    SIDE_LENGTH = 10

    @staticmethod
    def area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    sample_side = Square.SIDE_LENGTH
    calculated_area = Square.area(sample_side)
    print(calculated_area)