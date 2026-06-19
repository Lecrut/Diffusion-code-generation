class ComparisonTool:
    def check_greater(self, value1, value2):
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(10**10000, 999999999999999999)
    print(result)