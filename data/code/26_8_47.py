class ComparisonTool:

    def check_greater(self, value1, value2):
        try:
            return self._compare_values(value1, value2)
        except TypeError as e:
            raise ValueError('Both values must be comparable types') from e

    def _compare_values(self, value1, value2):
        if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
            return self._compare_numbers(value1, value2)
        elif isinstance(value1, str) and isinstance(value2, str):
            return self._compare_strings(value1, value2)
        else:
            raise TypeError('Unsupported types for comparison')

    def _compare_numbers(self, num1, num2):
        return num1 > num2

    def _compare_strings(self, str1, str2):
        return str1 > str2
if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(50, 25))
    print(tool.check_greater('apple', 'banana'))
    print(tool.check_greater([3, 4], [1, 2]))
    try:
        print(tool.check_greater('100', 50))
    except ValueError as e:
        print(e)