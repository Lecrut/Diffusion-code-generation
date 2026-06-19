class ComparisonTool:

    def check_greater(self, value1, value2):
        return value1 > value2
if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater(3, 7))