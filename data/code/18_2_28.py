class ComparisonTool:
    def __init__(self, value1, value2):
        self._first_value = value1
        self._second_value = value2

    def check_greater(self):
        return self._first_value > self._second_value

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 10
    SAMPLE_VALUE_2 = 5
    tool1 = ComparisonTool(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    result1 = tool1.check_greater()
    print(result1)

    SAMPLE_VALUE_3 = 3
    SAMPLE_VALUE_4 = 8
    tool2 = ComparisonTool(SAMPLE_VALUE_3, SAMPLE_VALUE_4)
    result2 = tool2.check_greater()
    print(result2)