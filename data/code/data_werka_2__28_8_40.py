class ComparisonTool:

    def __init__(self):
        self.comparison_operators = {'greater': lambda x, y: x > y, 'less': lambda x, y: x < y}

    def check_greater(self, value1, value2):
        return self.comparison_operators['greater'](value1, value2)
if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(20, 15)
    print(result)