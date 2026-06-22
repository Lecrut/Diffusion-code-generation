class ComparisonTool:
    def __init__(self):
        self.supported_types = (int, float)

    def validate_inputs(self, value1, value2):
        if not isinstance(value1, self.supported_types) or not isinstance(value2, self.supported_types):
            raise ValueError("Both values must be either int or float.")

    def check_greater(self, value1, value2):
        try:
            self.validate_inputs(value1, value2)
            return value1 > value2
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    tool = ComparisonTool()
    result1 = tool.check_greater(50, 45)
    print("Is 50 greater than 45?", result1)

    result2 = tool.check_greater('a', 'b')
    print("Is 'a' greater than 'b'?", result2)