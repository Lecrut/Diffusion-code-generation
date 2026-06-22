def is_temperature_difference_within_tolerance(temp1, temp2, tolerance=1):
    difference = abs(temp1 - temp2)
    return difference <= tolerance

class TemperatureDifferenceChecker:
    DEFAULT_TOLERANCE = 1
    def __init__(self, tolerance=None):
        self.tolerance = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE
    
    def check_difference(self, temp1, temp2):
        return is_temperature_difference_within_tolerance(temp1, temp2, self.tolerance)

if __name__ == '__main__':
    sample_temp1 = 15.0
    sample_temp2 = 14.8
    tolerance_value = 0.5
    
    result_function = is_temperature_difference_within_tolerance(sample_temp1, sample_temp2, tolerance_value)
    print("Function Result:", result_function)
    
    checker = TemperatureDifferenceChecker(tolerance=tolerance_value)
    result_class = checker.check_difference(sample_temp1, sample_temp2)
    print("Class Result:", result_class)