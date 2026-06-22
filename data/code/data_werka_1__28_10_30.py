class ComparisonTool:

    def check_greater(self, value1, value2):
        return value1 > value2
if __name__ == '__main__':
    tool = ComparisonTool()
    a = 150
    b = 149
    c = 3.14
    d = 3.14
    e = -10
    f = -20
    print(tool.check_greater(a, b))
    print(tool.check_greater(b, a))
    print(tool.check_greater(c, d))
    print(tool.check_greater(e, f))