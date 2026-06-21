class GeometryUtils:
    @staticmethod
    def calculate_square_side_length(area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        return area ** 0.5

if __name__ == '__main__':
    SAMPLE_AREA = 25.0
    side_length = GeometryUtils.calculate_square_side_length(SAMPLE_AREA)
    print(side_length)