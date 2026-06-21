def is_within_tolerance(temp1, temp2, tolerance=1):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Both temperature values must be numbers.")
    return abs(temp1 - temp2) <= tolerance

class TemperatureChecker:
    def __init__(self, tolerance=1):
        self.tolerance = tolerance
    
    def check(self, temp1, temp2):
        if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
            raise ValueError("Both temperature values must be numbers.")
        return abs(temp1 - temp2) <= self.tolerance

if __name__ == '__main__':
    try:
        temp1 = 30.5
        temp2 = 31.0
        result_function = is_within_tolerance(temp1, temp2)
        print("Function Result:", result_function)
        
        checker = TemperatureChecker()
        result_class = checker.check(temp1, temp2)
        print("Class Result:", result_class)
    except ValueError as e:
        print(e)