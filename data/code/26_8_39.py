class ComparisonTool:

    def check_greater(self, value1, value2):
        try:
            return value1 > value2
        except TypeError:
            raise ValueError('Both values must be comparable types')
if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater('b', 'a'))
    print(tool.check_greater([2, 3], [1]))
    try:
        print(tool.check_greater(10, 'a'))
    except ValueError as e:
        print(e)