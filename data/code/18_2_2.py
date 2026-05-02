class ComparisonTool:
    def __init__(self, a, b):
        self.attribute_a = a
        self.attribute_b = b
    def check_greater(self):
        return self.attribute_a > self.attribute_b
if __name__ == '__main__':
    a_val = 10
    b_val = 5
    tool = ComparisonTool(a_val, b_val)
    result = tool.check_greater()
    print(result)
    a_val = 3
    b_val = 8
    tool = ComparisonTool(a_val, b_val)
    result = tool.check_greater()
    print(result)
    a_val = 7
    b_val = 7
    tool = ComparisonTool(a_val, b_val)
    result = tool.check_greater()
    print(result)