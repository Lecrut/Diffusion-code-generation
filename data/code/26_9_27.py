class ComparisonTool:

    def check_greater(self, value1, value2):
        try:
            return value1 > value2
        except TypeError:
            return False
if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(10, 5)
    print(result)
    result = tool.check_greater('a', 'b')
    print(result)
    result = tool.check_greater([1, 2], [1])
    print(result)
    result = tool.check_greater(3.5, 4.0)
    print(result)
    result = tool.check_greater('abc', 123)
    print(result)