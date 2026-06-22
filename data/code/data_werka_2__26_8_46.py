class ComparisonTool:
    SUPPORTED_TYPES = (int, float, str, list, tuple, dict, set)

    def check_greater(self, value1, value2):
        if not isinstance(value1, self.SUPPORTED_TYPES) or not isinstance(value2, self.SUPPORTED_TYPES):
            raise ValueError('Both values must be comparable types')
        try:
            return value1 > value2
        except TypeError as e:
            raise ValueError(f'TypeError: {e}')
if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater('z', 'a'))
    print(tool.check_greater([3], [1, 2]))
    try:
        print(tool.check_greater('10', 5))
    except ValueError as e:
        print(e)