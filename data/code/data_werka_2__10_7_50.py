def check_temperature_difference(temp1, temp2, tolerance=1):
    difference = abs(temp1 - temp2)
    return difference <= tolerance

class TemperatureValidator:
    def __init__(self, tolerance=1):
        self.tolerance = tolerance
    
    def validate(self, temp1, temp2):
        return check_temperature_difference(temp1, temp2, self.tolerance)

if __name__ == '__main__':
    sample_temp_a = 15.0
    sample_temp_b = 14.8
    result_function = check_temperature_difference(sample_temp_a, sample_temp_b)
    print("Function Result:", result_function)
    
    validator = TemperatureValidator()
    result_class = validator.validate(sample_temp_a, sample_temp_b)
    print("Class Result:", result_class)