class TriangleCalculator:
    BASE_MULTIPLIER = 0.5

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def compute_area(self):
        return self.BASE_MULTIPLIER * self.base * self.height

    def get_dimensions(self):
        return (self.base, self.height)

if __name__ == '__main__':
    tri_instance = TriangleCalculator(base=8, height=4)
    area_result = tri_instance.compute_area()
    dim_result = tri_instance.get_dimensions()
    print(area_result)
    print(dim_result)