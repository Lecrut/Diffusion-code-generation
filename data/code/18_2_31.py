class ComparisonTool:
    DEFAULT_THRESHOLD = 0

    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2

    @staticmethod
    def compare_greater(a, b):
        return a > b

    def check_greater(self):
        return ComparisonTool.compare_greater(self._value1, self._value2)
if __name__ == '__main__':
    tool1 = ComparisonTool(10, 5)
    print(tool1.check_greater())
    tool2 = ComparisonTool(3, 7)
    print(tool2.check_greater())
    tool3 = ComparisonTool(8, 8)
    print(tool3.check_greater())
    tool4 = ComparisonTool(-5, -10)
    print(tool4.check_greater())