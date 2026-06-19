class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    sample_base = 7.0
    sample_height = 4.0
    shape_instance = Shape(sample_base, sample_height)
    area_result = shape_instance.calculate_area()
    print(area_result)