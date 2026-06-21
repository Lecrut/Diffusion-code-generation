class Square:
    MIN_AREA = 0

    @staticmethod
    def find_side_length(area):
        if area < Square.MIN_AREA:
            raise ValueError("Area cannot be negative")
        return area ** 0.5

if __name__ == '__main__':
    sample_area = 36
    side_length = Square.find_side_length(sample_area)
    print(f"The side length of the square with area {sample_area} is {side_length}")