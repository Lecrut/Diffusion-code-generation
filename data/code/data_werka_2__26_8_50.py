class ComparisonTool:

    def check_greater(self, value1, value2):
        try:
            return value1 > value2
        except TypeError:
            raise ValueError('Both values must be comparable types')
if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(10, 5)
    print(result)
    result = tool.check_greater('b', 'a')
    print(result)
    try:
        result = tool.check_greater([1, 2], [3])
        print(result)
    except ValueError as e:
        print(e)