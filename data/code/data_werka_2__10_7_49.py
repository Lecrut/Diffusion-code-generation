TEMPERATURE_DIFFERENCE_THRESHOLD = 1

def are_temperatures_close(temp1, temp2):
    return abs(temp1 - temp2) <= TEMPERATURE_DIFFERENCE_THRESHOLD

class TemperatureDifferenceChecker:

    def __init__(self, threshold=TEMPERATURE_DIFFERENCE_THRESHOLD):
        self.threshold = threshold

    def check_difference(self, temp1, temp2):
        return abs(temp1 - temp2) <= self.threshold
if __name__ == '__main__':
    sample_temp1 = 15.0
    sample_temp2 = 16.0
    result_function = are_temperatures_close(sample_temp1, sample_temp2)
    print('Function Result:', result_function)
    checker = TemperatureDifferenceChecker()
    result_class = checker.check_difference(sample_temp1, sample_temp2)
    print('Class Result:', result_class)