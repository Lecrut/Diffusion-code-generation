class ComparisonTool:
    def __init__(self):
        self.comparison_operations = {
            'greater': lambda x, y: x > y,
            'less': lambda x, y: x < y,
            'equal': lambda x, y: x == y
        }

    def validate_inputs(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise ValueError("Both values must be either int or float.")

    def check_greater(self, value1, value2):
        self.validate_inputs(value1, value2)
        return self.comparison_operations['greater'](value1, value2)

if __name__ == '__main__':
    tool = ComparisonTool()
    try:
        result = tool.check_greater(50, 45)
        print(result)
    except ValueError as e:
        print(e)