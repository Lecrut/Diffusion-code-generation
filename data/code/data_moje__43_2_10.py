class SquarePyramid:
    def __init__(self, side_length, slant_length):
        self.side_length = side_length
        self.slant_length = slant_length

    def get_base_area(self):
        return self.side_length * self.side_length

    def get_lateral_area(self):
        perimeter = self.side_length * 4
        half_perimeter = perimeter / 2.0
        return half_perimeter * self.slant_length

    def calculate_total_surface_area(self):
        base_component = self.get_base_area()
        lateral_component = self.get_lateral_area()
        return base_component + lateral_component

if __name__ == '__main__':
    base_value = 8.5
    slope_value = 10.25
    shape = SquarePyramid(base_value, slope_value)
    result = shape.calculate_total_surface_area()
    print(result)