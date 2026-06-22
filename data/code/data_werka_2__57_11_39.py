class Triangle:
    BASE = 6
    HEIGHT = 8

    def __init__(self, base=BASE, height=HEIGHT):
        self.base = base
        self.height = height

    @staticmethod
    def calculate_area(base, height):
        return 0.5 * base * height

    def get_area(self):
        return Triangle.calculate_area(self.base, self.height)

if __name__ == '__main__':
    triangle = Triangle()
    area = triangle.get_area()
    print(area)