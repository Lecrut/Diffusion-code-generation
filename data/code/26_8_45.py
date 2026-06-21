class ComparisonTool:
    COMPARABLE_TYPES = (int, float, str, list, tuple, dict, set)

    @staticmethod
    def is_comparable(value):
        return isinstance(value, ComparisonTool.COMPARABLE_TYPES)

    def check_greater(self, value1, value2):
        if not (ComparisonTool.is_comparable(value1) and ComparisonTool.is_comparable(value2)):
            raise ValueError('Both values must be comparable types')
        try:
            return value1 > value2
        except TypeError as e:
            return f'TypeError: {e}'

if __name__ == '__main__':
    tool = ComparisonTool()
    result1 = tool.check_greater(10, 5)
    result2 = tool.check_greater('world', 'hello')
    result3 = tool.check_greater([1, 2, 3], [1, 2])
    result4 = tool.check_greater({'a': 1}, {'b': 2})
    try:
        result5 = tool.check_greater('10', 5)
    except ValueError as e:
        result5 = str(e)

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)