class ComparisonTool:
    def check_greater(self, a, b):
        return a > b
if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater(3, 8))
    print(tool.check_greater(42, 100))
    print(tool.check_greater(15, 15))