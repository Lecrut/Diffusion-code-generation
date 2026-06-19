class Square:
    AREA = 25.0

    @staticmethod
    def calculate_side_length(area):
        return area ** 0.5

if __name__ == '__main__':
    side_length = Square.calculate_side_length(Square.AREA)
    print(f"The side length of the square is: {side_length}")