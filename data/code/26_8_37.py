class ComparisonTool:

    def check_greater(self, value1, value2):
        try:
            if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
                return value1 > value2
            else:
                raise ValueError('Both values must be either int or float.')
        except TypeError as e:
            return f'TypeError: {e}'
if __name__ == '__main__':
    tool = ComparisonTool()
    result1 = tool.check_greater(10, 5)
    result2 = tool.check_greater(3.5, 4.2)
    result3 = tool.check_greater('string', 5)
    print(result1)
    print(result2)
    print(result3)