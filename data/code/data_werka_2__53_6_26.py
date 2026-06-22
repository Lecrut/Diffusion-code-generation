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
    sample_area_value = 36
    square_properties = SquareProperties(sample_area_value)
    side_length_result = square_properties.get_side_length()
    print(f"The side length of a square with area {sample_area_value} is {side_length_result}")