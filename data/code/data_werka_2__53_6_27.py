def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

class Square:
    def __init__(self, area):
        self.area = area
    def side_length(self):
        return find_side_length(self.area)

if __name__ == '__main__':
    sample_areas = [9, 16, 25]
    for area in sample_areas:
        square = Square(area)
        print(f"The side length of a square with area {area} is {square.side_length()}")