class Prism:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def get_volume(self):
        return self.base_area * self.height

if __name__ == '__main__':
    prism = Prism(25, 10)
    print(prism.get_volume())