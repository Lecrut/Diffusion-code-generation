class Prism:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def get_volume(self):
        return self.base_area * self.height

    def get_dimensions(self):
        return (self.base_area, self.height)

if __name__ == '__main__':
    prism_instance = Prism(24.5, 12.0)
    calculated_volume = prism_instance.get_volume()
    dims = prism_instance.get_dimensions()
    print(calculated_volume)
    print(dims)