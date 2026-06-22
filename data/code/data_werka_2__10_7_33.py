TEMPERATURE_TOLERANCE = 1

def compare_temperatures(temp1, temp2):
    return abs(temp1 - temp2) <= TEMPERATURE_TOLERANCE

class TemperatureComparator:

    def __init__(self, tolerance=TEMPERATURE_TOLERANCE):
        self.tolerance = tolerance

    def are_within_tolerance(self, temp1, temp2):
        return abs(temp1 - temp2) <= self.tolerance
if __name__ == '__main__':
    sample_temperatures = {'temp1': 25.0, 'temp2': 24.5}
    result_func = compare_temperatures(sample_temperatures['temp1'], sample_temperatures['temp2'])
    print('Function Result:', result_func)
    comparator = TemperatureComparator()
    result_class = comparator.are_within_tolerance(sample_temperatures['temp1'], sample_temperatures['temp2'])
    print('Class Result:', result_class)