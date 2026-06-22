class SquareUtils:
    @staticmethod
    def calculate_side_length(area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        return area ** 0.5

if __name__ == '__main__':
    AREA_VALUE = 25.0
    try:
        side_length = SquareUtils.calculate_side_length(AREA_VALUE)
        print(side_length)
    except ValueError as e:
        print(e)