class TemperatureDifferenceChecker:

    def __init__(self, tolerance=1):
        self.tolerance = tolerance

    def is_within_tolerance(self, temp1, temp2):
        return abs(temp1 - temp2) <= self.tolerance
if __name__ == '__main__':
    sample_temp1 = 15.0
    sample_temp2 = 16.3
    checker = TemperatureDifferenceChecker()
    result_default_tolerance = checker.is_within_tolerance(sample_temp1, sample_temp2)
    print('Are temperatures within default tolerance?', result_default_tolerance)
    new_tolerance = 2
    checker.tolerance = new_tolerance
    result_new_tolerance = checker.is_within_tolerance(sample_temp1, sample_temp2)
    print(f'Are temperatures within {new_tolerance} degree tolerance?', result_new_tolerance)