class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    triangle = Triangle(sample_base, sample_height)
    print(triangle.calculate_area())