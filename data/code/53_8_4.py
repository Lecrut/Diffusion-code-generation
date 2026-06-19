class Square:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def find_side_length(self):
        return self.area ** 0.5

if __name__ == '__main__':
    sample_areas = [16, 49, 81]
    for area in sample_areas:
        try:
            square = Square(area)
            side_length = square.find_side_length()
            print(f"The side length of the square with area {area} is: {side_length}")
        except ValueError as e:
            print(e)