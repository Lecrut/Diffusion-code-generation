class Prism:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def get_volume(self):
        return self.base_area * self.height

if __name__ == '__main__':
    base_area = 50
    height = 10
    prism = Prism(base_area, height)
    print(prism.get_volume())