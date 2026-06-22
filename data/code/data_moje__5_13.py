import math

class Measurement:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

class LengthComparator:
    def __init__(self):
        self.m1 = Measurement(10.0, "meters")
        self.m2 = Measurement(10.0 + 1e-9, "meters")
        self.epsilon = 1e-5

    def is_equal_epsilon(self):
        diff = abs(self.m1.value - self.m2.value)
        return diff < self.epsilon

    def get_absolute_difference(self):
        return abs(self.m1.value - self.m2.value)

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.is_equal_epsilon())
    print(comparator.get_absolute_difference())