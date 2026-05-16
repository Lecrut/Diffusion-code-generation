class GeometryUtils:
    @staticmethod
    def calculate_perimeter(length: float, width: float) -> float:
        return 2 * (length + width)
if __name__ == '__main__':
    sample_length = 10.0
    sample_width = 5.0
    perimeter = GeometryUtils.calculate_perimeter(sample_length, sample_width)
    print(perimeter)