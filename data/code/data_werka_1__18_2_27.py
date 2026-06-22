class ComparisonTool:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def compare_greater(value1, value2):
        return value1 > value2

    def check_greater(self):
        return self.compare_greater(self.value1, self.value2)
if __name__ == '__main__':
    tool1 = ComparisonTool(15, 10)
    result1 = tool1.check_greater()
    print(result1)
    tool2 = ComparisonTool(4, 8)
    result2 = tool2.check_greater()
    print(result2)