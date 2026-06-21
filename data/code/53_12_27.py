import math

def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

class SquareProperties:
    def __init__(self, area):
        self.area = area
    
    def get_side_length(self):
        return calculate_square_side_length(self.area)
    
    def get_description(self):
        side_length = self.get_side_length()
        return f"Square with area {self.area} has a side length of {side_length}"

if __name__ == '__main__':
    sample_areas = {
        "small": 9.0,
        "medium": 16.0,
        "large": 25.0
    }
    
    for description, area in sample_areas.items():
        try:
            square = SquareProperties(area)
            print(square.get_description())
        except ValueError as e:
            print(e)