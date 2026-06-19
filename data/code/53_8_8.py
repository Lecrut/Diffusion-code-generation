class Square:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def find_side_length(self):
        return self.area ** 0.5

if __name__ == '__main__':
    sample_areas = {
        'small': 9,
        'medium': 25,
        'large': 49
    }
    for description, area in sample_areas.items():
        try:
            square = Square(area)
            side_length = square.find_side_length()
            print(f"The side length of the {description} square with area {area} is: {side_length}")
        except ValueError as e:
            print(e)