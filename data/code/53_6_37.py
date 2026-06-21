def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

class SquareProperties:
    def __init__(self, area):
        self.area = area
    
    def get_side_length(self):
        return find_side_length(self.area)

if __name__ == '__main__':
    SAMPLE_AREAS = [9, 16, 25, 49]
    for area in SAMPLE_AREAS:
        square = SquareProperties(area)
        side_length = square.get_side_length()
        print(f"The side length of a square with area {area} is {side_length}")