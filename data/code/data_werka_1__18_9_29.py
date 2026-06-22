class ComparisonTool:
    def check_greater(self, value1, value2):
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(987654321012345678901234567890, 123456789012345678901234567890)
    print(result)