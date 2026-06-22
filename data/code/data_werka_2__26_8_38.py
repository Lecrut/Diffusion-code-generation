class ComparisonTool:

    def check_greater(self, value1, value2):
        if not self._can_compare(value1, value2):
            raise ValueError('Both values must be comparable types')
        return value1 > value2

    def _can_compare(self, value1, value2):
        try:
            return value1 > value2
        except TypeError:
            return False
if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater('b', 'a'))
    print(tool.check_greater([3], [1, 2]))
    try:
        print(tool.check_greater('10', 5))
    except ValueError as e:
        print(e)
    print(tool.check_greater(3.5, 2.5))