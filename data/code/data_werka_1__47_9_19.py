class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
if __name__ == '__main__':
    sample_base = 7.0
    sample_height = 4.0
    triangle = Triangle(sample_base, sample_height)
    area = triangle.calculate_area()
    print(area)