class ComparisonTool:
    def check_greater(self, value1, value2):
        return value1 > value2

if __name__ == '__main__':
    comparison_tool = ComparisonTool()
    print(comparison_tool.check_greater(10, 5))
    print(comparison_tool.check_greater(5, 10))
    print(comparison_tool.check_greater(7.5, 7.5))
    print(comparison_tool.check_greater(200, 199))
    print(comparison_tool.check_greater(-1, -5))