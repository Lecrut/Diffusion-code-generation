class ComparisonTool:
    def __init__(self, attr1, attr2):
        self._attribute1 = attr1
        self._attribute2 = attr2
    def check_greater(self):
        return self._attribute1 > self._attribute2
if __name__ == '__main__':
    a = 10
    b = 5
    tool = ComparisonTool(a, b)
    result = tool.check_greater()
    print(result)
    c = 3
    d = 7
    tool2 = ComparisonTool(c, d)
    result2 = tool2.check_greater()
    print(result2)