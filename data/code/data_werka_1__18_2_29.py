class ComparisonTool:
    def __init__(self, first_value, second_value):
        self._first_value = first_value
        self._second_value = second_value

    def check_greater(self):
        return self._first_value > self._second_value

if __name__ == '__main__':
    value1 = 20
    value2 = 15
    comparison_tool = ComparisonTool(value1, value2)
    is_greater = comparison_tool.check_greater()
    print(is_greater)

    value3 = 8
    value4 = 25
    another_comparison_tool = ComparisonTool(value3, value4)
    result = another_comparison_tool.check_greater()
    print(result)