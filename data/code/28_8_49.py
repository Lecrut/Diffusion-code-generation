class ComparisonTool:
    def check_greater(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise ValueError("Both values must be either int or float.")
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()
    try:
        result = tool.check_greater(50, 45)
        print(result)
    except ValueError as e:
        print(e)