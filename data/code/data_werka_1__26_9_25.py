class ComparisonTool:

    def check_greater(self, value1, value2):
        try:
            return value1 > value2
        except TypeError as e:
            print(f'TypeError: {e}')
            return None
if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(10, 5)
    print(result)
    result = tool.check_greater('a', 'b')
    print(result)
    result = tool.check_greater([1, 2], [3])
    print(result)
    result = tool.check_greater(10, 'a')
    print(result)