class ComparisonTool:

    def check_greater(self, value1, value2):
        try:
            return self._compare_values(value1, value2)
        except TypeError:
            raise ValueError('Both values must be comparable types')

    def _compare_values(self, value1, value2):
        if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
            return value1 > value2
        elif isinstance(value1, str) and isinstance(value2, str):
            return value1 > value2
        elif isinstance(value1, list) and isinstance(value2, list):
            return len(value1) > len(value2)
        else:
            raise TypeError('Unsupported types for comparison')
if __name__ == '__main__':
    tool = ComparisonTool()
    result1 = tool.check_greater(20, 15)
    result2 = tool.check_greater('apple', 'banana')
    result3 = tool.check_greater([1, 2, 3], [4, 5])
    print(result1)
    print(result2)
    print(result3)