class Measurement:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

class LengthComparator:
    def __init__(self, measurement1, measurement2):
        self.measurement1 = measurement1
        self.measurement2 = measurement2

    def are_equal(self, epsilon=1e-9):
        return abs(self.measurement1.value - self.measurement2.value) < epsilon

    def absolute_difference(self):
        return abs(self.measurement1.value - self.measurement2.value)

if __name__ == '__main__':
    m1 = Measurement(1.0, 'meters')
    m2 = Measurement(1.000000001, 'meters')
    comparator = LengthComparator(m1, m2)
    print(comparator.are_equal())
    print(comparator.absolute_difference())