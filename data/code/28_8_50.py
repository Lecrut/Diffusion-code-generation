class ComparisonTool:
    SUPPORTED_TYPES = (int, float)

    @staticmethod
    def validate_inputs(value1, value2):
        if not isinstance(value1, ComparisonTool.SUPPORTED_TYPES) or not isinstance(value2, ComparisonTool.SUPPORTED_TYPES):
            raise ValueError("Both values must be either int or float.")

    def check_greater(self, value1, value2):
        ComparisonTool.validate_inputs(value1, value2)
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()
    try:
        result = tool.check_greater(50.5, 45)
        print(result)
    except ValueError as e:
        print(e)