class ComparisonTool:
    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2

    def check_greater(self):
        return self._value1 > self._value2

if __name__ == '__main__':
    first_value = 25
    second_value = 10
    comparison_tool_1 = ComparisonTool(first_value, second_value)
    is_first_greater_than_second = comparison_tool_1.check_greater()
    print(is_first_greater_than_second)

    third_value = 8
    fourth_value = 12
    comparison_tool_2 = ComparisonTool(third_value, fourth_value)
    is_third_greater_than_fourth = comparison_tool_2.check_greater()
    print(is_third_greater_than_fourth)