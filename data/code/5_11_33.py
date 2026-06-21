class MeasurementComparator:
    DEFAULT_LENGTH1 = 20.5
    DEFAULT_LENGTH2 = 8.7

    @staticmethod
    def calculate_difference(length1, length2):
        return length1 - length2

    @staticmethod
    def calculate_ratio(length1, length2):
        if length2 == 0:
            return float('inf')
        return length1 / length2

    @staticmethod
    def is_first_greater(length1, length2):
        return length1 > length2

    @staticmethod
    def compare_measurements(length1, length2):
        difference = MeasurementComparator.calculate_difference(length1, length2)
        ratio = MeasurementComparator.calculate_ratio(length1, length2)
        is_greater = MeasurementComparator.is_first_greater(length1, length2)
        return difference, ratio, is_greater

if __name__ == '__main__':
    length1 = MeasurementComparator.DEFAULT_LENGTH1
    length2 = MeasurementComparator.DEFAULT_LENGTH2
    result = MeasurementComparator.compare_measurements(length1, length2)
    print(result)