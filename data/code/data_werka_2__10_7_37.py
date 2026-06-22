TEMPERATURE_TOLERANCE = 1

def are_temperatures_close(temp1, temp2, tolerance=TEMPERATURE_TOLERANCE):
    return abs(temp1 - temp2) <= tolerance

class TemperatureDifferenceChecker:
    def __init__(self, tolerance=TEMPERATURE_TOLERANCE):
        self.tolerance = tolerance
    
    def check_difference(self, temp1, temp2):
        return abs(temp1 - temp2) <= self.tolerance

if __name__ == '__main__':
    sample_temperatures = {
        'morning': 15.0,
        'afternoon': 16.0
    }
    
    result_function = are_temperatures_close(sample_temperatures['morning'], sample_temperatures['afternoon'])
    print("Function Result:", result_function)
    
    checker = TemperatureDifferenceChecker()
    result_class = checker.check_difference(sample_temperatures['morning'], sample_temperatures['afternoon'])
    print("Class Result:", result_class)