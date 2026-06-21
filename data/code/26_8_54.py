class ComparisonTool:

    def __init__(self):
        self.supported_types = (int, float, str, list, tuple, dict, set)

    def is_supported(self, value):
        return isinstance(value, self.supported_types)

    def check_greater(self, value1, value2):
        if not (self.is_supported(value1) and self.is_supported(value2)):
            raise ValueError('Both values must be comparable types')
        try:
            return value1 > value2
        except TypeError as e:
            raise ValueError(f'TypeError: {e}')
if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater('b', 'a'))
    print(tool.check_greater([2, 3], [1]))
    try:
        print(tool.check_greater('10', 5))
    except ValueError as e:
        print(e)
    print(tool.check_greater(3.5, 4.2))
    print(tool.check_greater({'key': 'value'}, {}))
    print(tool.check_greater({1, 2}, {0}))