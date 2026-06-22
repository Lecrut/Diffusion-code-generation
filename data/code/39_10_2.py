class Prism:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def volume(self):
        return self.base_area * self.height

if __name__ == '__main__':
    base_area = 10.0
    height = 5.0
    prism = Prism(base_area, height)
    print(prism.volume())