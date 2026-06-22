class GeometryHelper:
    @staticmethod
    def calculate_square_area(side):
        return side ** 2

if __name__ == '__main__':
    sample_side_length = 7
    print(GeometryHelper.calculate_square_area(sample_side_length))