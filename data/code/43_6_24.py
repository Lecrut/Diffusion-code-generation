class Square:
    @staticmethod
    def calculate_area(side):
        return side * side

if __name__ == '__main__':
    sample_side_length = 7
    area = Square.calculate_area(sample_side_length)
    print(area)