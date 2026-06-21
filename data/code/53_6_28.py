class Square:
    MIN_AREA = 0

    @staticmethod
    def calculate_side_length(area):
        if area < Square.MIN_AREA:
            raise ValueError("Area cannot be negative")
        return area ** 0.5

if __name__ == '__main__':
    sample_areas = {
        "tiny": 4,
        "standard": 100,
        "huge": 81
    }
    for description, area in sample_areas.items():
        try:
            side_length = Square.calculate_side_length(area)
            print(f"The side length of the {description} square is {side_length}")
        except ValueError as e:
            print(e)