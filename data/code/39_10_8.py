class Prism:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def volume(self):
        return self.base_area * self.height

if __name__ == '__main__':
    base_area_value = 50
    height_value = 10
    my_prism = Prism(base_area_value, height_value)
    print(my_prism.volume())