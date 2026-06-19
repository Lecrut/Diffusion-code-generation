class ComparisonTool:

    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2

    def check_greater(self):
        return self._value1 > self._value2
if __name__ == '__main__':
    tool1 = ComparisonTool(15, 10)
    print(tool1.check_greater())
    tool2 = ComparisonTool(4, 8)
    print(tool2.check_greater())