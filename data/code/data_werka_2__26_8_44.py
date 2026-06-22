class ComparisonTool:

    def check_greater(self, value1, value2):
        try:
            if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
                return value1 > value2
            else:
                raise ValueError('Both values must be either int or float.')
        except TypeError as e:
            print(f'TypeError: {e}')
            return False
if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(10, 5)
    print(result)