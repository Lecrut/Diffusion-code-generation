class ComparisonTool:
    @staticmethod
    def check_greater(a, b):
        return a > b

if __name__ == '__main__':
    print(ComparisonTool.check_greater(10, 5))
    print(ComparisonTool.check_greater(5, 10))
    print(ComparisonTool.check_greater(7.5, 7.5))
    print(ComparisonTool.check_greater(200, 199))
    print(ComparisonTool.check_greater(-1, -5))