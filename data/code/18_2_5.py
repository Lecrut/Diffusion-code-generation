class ComparisonTool:
    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2
    def check_greater(self):
        return self._value1 > self._value2
if __name__ == '__main__':
    a = 10
    b = 5
    tool1 = ComparisonTool(a, b)
    print(f"Is {a} greater than {b}? {tool1.check_greater()}")
    c = 3
    d = 8
    tool2 = ComparisonTool(c, d)
    print(f"Is {c} greater than {d}? {tool2.check_greater()}")
    e = 7
    f = 7
    tool3 = ComparisonTool(e, f)
    print(f"Is {e} greater than {f}? {tool3.check_greater()}")