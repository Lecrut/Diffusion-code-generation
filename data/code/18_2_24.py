class ComparisonTool:
    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2

    def check_greater(self):
        return self._value1 > self._value2

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 20
    SAMPLE_VALUE_2 = 15
    tool = ComparisonTool(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    result = tool.check_greater()
    print(result)

    SAMPLE_VALUE_3 = 8
    SAMPLE_VALUE_4 = 12
    tool2 = ComparisonTool(SAMPLE_VALUE_3, SAMPLE_VALUE_4)
    result2 = tool2.check_greater()
    print(result2)