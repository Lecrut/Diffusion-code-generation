class ComparisonTool:
    def check_greater(self, a, b):
        try:
            return a > b
        except TypeError:
            return False
if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater(3, 8))
    print(tool.check_greater("hello", "world"))
    print(tool.check_greater(10.5, 10))
    print(tool.check_greater([1], 0))