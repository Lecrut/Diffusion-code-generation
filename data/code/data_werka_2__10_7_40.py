def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be a number.")

def are_temperatures_within_tolerance(temp1, temp2, tolerance=1):
    validate_temperature(temp1)
    validate_temperature(temp2)
    return abs(temp1 - temp2) <= tolerance

class TemperatureComparator:
    def __init__(self, tolerance=1):
        self.tolerance = tolerance
        validate_temperature(self.tolerance)

    def compare(self, temp1, temp2):
        validate_temperature(temp1)
        validate_temperature(temp2)
        return abs(temp1 - temp2) <= self.tolerance

if __name__ == '__main__':
    temp1 = 27.3
    temp2 = 28.0
    result_function = are_temperatures_within_tolerance(temp1, temp2)
    print("Function Result:", result_function)

    comparator = TemperatureComparator(tolerance=2)
    result_class = comparator.compare(temp1, temp2)
    print("Class Result:", result_class)