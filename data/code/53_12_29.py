import math

class Square:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def calculate_side_length(self):
        return math.sqrt(self.area)

if __name__ == '__main__':
    sample_area1 = 49.0
    sample_area2 = 64.0
    try:
        square1 = Square(sample_area1)
        side_length1 = square1.calculate_side_length()
        print(f"Side length for area {sample_area1}: {side_length1}")

        square2 = Square(sample_area2)
        side_length2 = square2.calculate_side_length()
        print(f"Side length for area {sample_area2}: {side_length2}")
    except ValueError as e:
        print(e)