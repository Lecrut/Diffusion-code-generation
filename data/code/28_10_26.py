class ComparisonTool:
    def check_greater(self, a, b):
        return a > b

if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater(5, 10))
    print(tool.check_greater(7.5, 7.5))
    print(tool.check_greater(200, 199))
    print(tool.check_greater(-1, -5))