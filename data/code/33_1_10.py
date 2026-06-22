class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def compute_area(self):
        return self.base * self.height / 2

    def get_base(self):
        return self.base

    def get_height(self):
        return self.height

if __name__ == '__main__':
    tri = Triangle(base=8, height=12)
    print(tri.compute_area())
    print(tri.get_base())
    print(tri.get_height())