class ComparisonTool:
    def check_greater(self, value1, value2):
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(98765432109876543210, 12345678901234567890)
    print(result)