RECTANGLE_CONFIG = {
    "length": 14,
    "width": 6
}

class GeometryCalculator:
    @staticmethod
    def calculate_area(dimensions):
        length = dimensions.get("length")
        width = dimensions.get("width")
        if length is None or width is None:
            raise ValueError("Dimensions must include both length and width.")
        return length * width

if __name__ == '__main__':
    try:
        area = GeometryCalculator.calculate_area(RECTANGLE_CONFIG)
        print(area)
    except ValueError as e:
        print(e)