class ComparisonTool:
    def check_greater(self, value1, value2):
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(10**1000, 999**999)
    print(result)