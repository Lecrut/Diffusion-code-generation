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
    
    def get_area_category(self):
        categories = {
            "small": (0, 10),
            "medium": (10, 50),
            "large": (50, float('inf'))
        }
        for category, (min_area, max_area) in categories.items():
            if min_area <= self.area < max_area:
                return category
        return "unknown"

if __name__ == '__main__':
    sample_areas = [16.0, 25.0, 36.0, -4.0]
    for area in sample_areas:
        try:
            properties = SquareProperties(area)
            side_length = properties.get_side_length()
            category = properties.get_area_category()
            print(f"Area: {area}, Side Length: {side_length}, Category: {category}")
        except ValueError as e:
            print(f"Error for area {area}: {e}")