class ComparisonTool:
    def check_greater(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise ValueError("Both values must be integers or floats")
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(1000000000000000000000000, 999999999999999999999999)
    print(result)