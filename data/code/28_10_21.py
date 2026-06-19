class ComparisonTool:
    def check_greater(self, a, b):
        return a > b

if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(10, 5)
    print(result)