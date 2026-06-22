class Prism:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def volume(self):
        return self.base_area * self.height

if __name__ == '__main__':
    my_prism = Prism(15, 10)
    print(my_prism.volume())