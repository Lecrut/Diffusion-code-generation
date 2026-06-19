class ComparisonTool:

    def __init__(self, value1, value2):
        self._first_value = value1
        self._second_value = value2

    def check_greater(self):
        return self._first_value > self._second_value
if __name__ == '__main__':
    VALUE_A = 20
    VALUE_B = 15
    tool1 = ComparisonTool(VALUE_A, VALUE_B)
    result1 = tool1.check_greater()
    print(result1)
    VALUE_C = 8
    VALUE_D = 12
    tool2 = ComparisonTool(VALUE_C, VALUE_D)
    result2 = tool2.check_greater()
    print(result2)