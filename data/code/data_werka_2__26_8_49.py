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
        except TypeError:
            raise ValueError(f'Unexpected error comparing {value1} and {value2}')
if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater('b', 'a'))
    print(tool.check_greater([3], [1, 2]))
    try:
        print(tool.check_greater('10', 5))
    except ValueError as e:
        print(e)