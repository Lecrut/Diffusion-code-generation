class ComparisonTool:
    def check_value_equality(self, x, y):
        return x == y
if __name__ == '__main__':
    tool = ComparisonTool()
    x1 = 5
    y1 = 5
    result1 = tool.check_value_equality(x1, y1)
    print(f"Checking equality between {x1} and {y1}: {result1}")
    x2 = 10
    y2 = 20
    result2 = tool.check_value_equality(x2, y2)
    print(f"Checking equality between {x2} and {y2}: {result2}")
    x3 = 3.14
    y3 = 3.14
    result3 = tool.check_value_equality(x3, y3)
    print(f"Checking equality between {x3} and {y3}: {result3}")
    x4 = 1.0
    y4 = 1.0000000000000001
    result4 = tool.check_value_equality(x4, y4)
    print(f"Checking equality between {x4} and {y4}: {result4}")
    x5 = 5
    y5 = "5"
    result5 = tool.check_value_equality(x5, y5)
    print(f"Checking equality between {x5} and '{y5}': {result5}")