class Prism:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def get_volume(self):
        return self.base_area * self.height

if __name__ == '__main__':
    sample_base_area = 25
    sample_height = 10
    prism = Prism(sample_base_area, sample_height)
    volume = prism.get_volume()
    print(volume)