class ComparisonTool:
    def __init__(self):
        self.supported_types = (int, float)

    def validate_inputs(self, value1, value2):
        if not isinstance(value1, self.supported_types) or not isinstance(value2, self.supported_types):
            raise ValueError("Both values must be either int or float.")

    def check_greater(self, value1, value2):
        self.validate_inputs(value1, value2)
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()
    try:
        result = tool.check_greater(30.5, 25)
        print(result)
    except ValueError as e:
        print(e)