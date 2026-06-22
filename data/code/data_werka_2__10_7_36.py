def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be a number.")

def are_temperatures_within_tolerance(temp1, temp2, tolerance=1):
    validate_temperature(temp1)
    validate_temperature(temp2)
    return abs(temp1 - temp2) <= tolerance

class TemperatureComparer:
    DEFAULT_TOLERANCE = 1
    def __init__(self, tolerance=DEFAULT_TOLERANCE):
        self.tolerance = tolerance
    
    def set_tolerance(self, new_tolerance):
        validate_temperature(new_tolerance)
        self.tolerance = new_tolerance
    
    def compare(self, temp1, temp2):
        validate_temperature(temp1)
        validate_temperature(temp2)
        return abs(temp1 - temp2) <= self.tolerance

if __name__ == '__main__':
    sample_temp1 = 22.0
    sample_temp2 = 23.5
    result_function = are_temperatures_within_tolerance(sample_temp1, sample_temp2)
    print("Function Result:", result_function)
    
    comparer = TemperatureComparer()
    result_class = comparer.compare(sample_temp1, sample_temp2)
    print("Class Result with default tolerance:", result_class)
    
    comparer.set_tolerance(2.0)
    result_class_new_tolerance = comparer.compare(sample_temp1, sample_temp2)
    print("Class Result with new tolerance:", result_class_new_tolerance)