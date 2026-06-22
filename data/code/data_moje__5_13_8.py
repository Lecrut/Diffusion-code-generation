class LengthComparator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.epsilon = 1e-9

    def are_equal(self):
        diff = abs(self.value1 - self.value2)
        return diff <= self.epsilon

    def absolute_difference(self):
        return abs(self.value1 - self.value2)

if __name__ == '__main__':
    lc = LengthComparator(10.000000001, 10.000000002)
    print(lc.are_equal())
    print(lc.absolute_difference())