class Square:
    MIN_AREA = 0

    @staticmethod
    def find_side_length(area):
        if area < Square.MIN_AREA:
            raise ValueError("Area cannot be negative")
        return area ** 0.5

if __name__ == '__main__':
    sample_areas = [9, 16, 25]
    for area in sample_areas:
        side_length = Square.find_side_length(area)
        print(f"The side length of a square with area {area} is {side_length}")