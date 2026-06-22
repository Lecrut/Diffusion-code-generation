class MeasurementComparer:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def calculate_difference(self):
        return self.length1 - self.length2

    def calculate_ratio(self):
        if self.length2 == 0:
            return float('inf')
        return self.length1 / self.length2

    def is_first_greater(self):
        return self.length1 > self.length2

if __name__ == '__main__':
    length1 = 7.8
    length2 = 4.6
    comparer = MeasurementComparer(length1, length2)
    difference = comparer.calculate_difference()
    ratio = comparer.calculate_ratio()
    is_greater = comparer.is_first_greater()
    print(difference)
    print(ratio)
    print(is_greater)