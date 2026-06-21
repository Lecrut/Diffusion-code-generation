class ComparisonTool:

    def __init__(self):
        self.type_hierarchy = {int: 1, float: 2, str: 3, list: 4, tuple: 5, dict: 6, set: 7}

    def _is_comparable(self, value):
        return type(value) in self.type_hierarchy

    def check_greater(self, value1, value2):
        if not (self._is_comparable(value1) and self._is_comparable(value2)):
            raise ValueError('Both values must be comparable types')
        if self.type_hierarchy[type(value1)] != self.type_hierarchy[type(value2)]:
            return type(value1).__name__ > type(value2).__name__
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
    print(tool.check_greater((1, 2), (1,)))
    print(tool.check_greater({'a': 1}, {'b'}))