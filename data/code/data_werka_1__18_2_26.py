class ComparisonTool:
    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2

    def check_greater(self):
        return self._value1 > self._value2

if __name__ == '__main__':
    sample_values = [
        (10, 5),
        (3, 7),
        (8, 8),
        (15, 20)
    ]

    for val1, val2 in sample_values:
        tool = ComparisonTool(val1, val2)
        result = tool.check_greater()
        print(f"{val1} > {val2}: {result}")