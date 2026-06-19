class AreaCalculator:
    def __init__(self, dimensions):
        self.length = dimensions['length']
        self.width = dimensions['width']

    @property
    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    sample_dimensions = {'length': 9, 'width': 6}
    calculator = AreaCalculator(sample_dimensions)
    print(calculator.area)