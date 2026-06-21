TEMPERATURE_TOLERANCE = 1

def are_temperatures_within_tolerance(temp1, temp2):
    return abs(temp1 - temp2) <= TEMPERATURE_TOLERANCE

class TemperatureComparator:
    def __init__(self, tolerance=TEMPERATURE_TOLERANCE):
        self.tolerance = tolerance
    
    def compare(self, temp1, temp2):
        return abs(temp1 - temp2) <= self.tolerance

if __name__ == '__main__':
    sample_temp1 = 15.0
    sample_temp2 = 16.3
    result_function = are_temperatures_within_tolerance(sample_temp1, sample_temp2)
    print("Function Result:", result_function)
    
    comparator = TemperatureComparator()
    result_class = comparator.compare(sample_temp1, sample_temp2)
    print("Class Result:", result_class)