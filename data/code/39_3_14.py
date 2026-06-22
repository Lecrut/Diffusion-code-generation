VOLUME_UNIT = 1.0

class GeometricPrism:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def get_volume(self):
        return self.base_area * self.height * VOLUME_UNIT

if __name__ == '__main__':
    my_prism = GeometricPrism(20.0, 8.0)
    computed_volume = my_prism.get_volume()
    print(computed_volume)