class Measurement:
    def __init__(self, value):
        self.value = value

class LengthComparator:
    def __init__(self, measurement1, measurement2, epsilon=1e-9):
        self.measurement1 = measurement1
        self.measurement2 = measurement2
        self.epsilon = epsilon

    def are_equal_within_epsilon(self):
        return abs(self.measurement1.value - self.measurement2.value) < self.epsilon

    def absolute_difference(self):
        return abs(self.measurement1.value - self.measurement2.value)

if __name__ == '__main__':
    measurement_a = Measurement(3.141592653589793)
    measurement_b = Measurement(3.1415926535897932)
    
    comparator = LengthComparator(measurement_a, measurement_b)
    print(comparator.are_equal_within_epsilon())
    print(comparator.absolute_difference())