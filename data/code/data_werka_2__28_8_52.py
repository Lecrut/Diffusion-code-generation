class ComparisonTool:
    def __init__(self):
        self.supported_types = (int, float)
    
    def validate_inputs(self, value1, value2):
        if not isinstance(value1, self.supported_types) or not isinstance(value2, self.supported_types):
            raise ValueError("Both values must be either int or float.")
    
    def perform_greater_check(self, value1, value2):
        return value1 > value2
    
    def check_greater(self, value1, value2):
        self.validate_inputs(value1, value2)
        result = self.perform_greater_check(value1, value2)
        return result

if __name__ == '__main__':
    tool = ComparisonTool()
    try:
        value1 = 50
        value2 = 45
        result = tool.check_greater(value1, value2)
        print(f"Is {value1} greater than {value2}?", result)
    except ValueError as e:
        print(e)