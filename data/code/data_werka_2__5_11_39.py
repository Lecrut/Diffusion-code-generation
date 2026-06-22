class MeasurementComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def calculate_difference(self):
        return self.length1 - self.length2

    def calculate_ratio(self):
        if self.length2 == 0:
            raise ValueError("Length2 cannot be zero for ratio calculation.")
        return self.length1 / self.length2

    def is_first_greater(self):
        return self.length1 > self.length2

def compare_measurements(length1, length2):
    comparator = MeasurementComparator(length1, length2)
    difference = comparator.calculate_difference()
    ratio = comparator.calculate_ratio()
    is_greater = comparator.is_first_greater()
    return difference, ratio, is_greater

if __name__ == '__main__':
    length1 = 20.7
    length2 = 5.4
    try:
        result = compare_measurements(length1, length2)
        print(result)
    except ValueError as e:
        print(e)