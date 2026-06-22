class RectangularSurface:
    def __init__(self, dimension_a, dimension_b):
        self.d_a = dimension_a
        self.d_b = dimension_b

    def compute_surface_area(self):
        return self.d_a * self.d_b

    def get_dimensions(self):
        return self.d_a, self.d_b

if __name__ == '__main__':
    surface = RectangularSurface(8.5, 4.0)
    area_result = surface.compute_surface_area()
    print(area_result)
    dims_result = surface.get_dimensions()
    print(dims_result)