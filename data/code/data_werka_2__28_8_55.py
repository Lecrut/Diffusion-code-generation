class ComparisonTool:
    def __init__(self):
        self.comparison_methods = {
            'greater': lambda x, y: x > y,
            'less': lambda x, y: x < y,
            'equal': lambda x, y: x == y
        }
    
    def validate_inputs(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise ValueError("Both values must be either int or float.")
    
    def check_greater(self, value1, value2):
        self.validate_inputs(value1, value2)
        return self.comparison_methods['greater'](value1, value2)

if __name__ == '__main__':
    tool = ComparisonTool()
    try:
        result1 = tool.check_greater(50, 45)
        print("Is 50 greater than 45?", result1)
        
        result2 = tool.check_greater(30, 35)
        print("Is 30 greater than 35?", result2)
    except ValueError as e:
        print(e)