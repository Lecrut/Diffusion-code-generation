class ComparisonTool:
    def check_greater(self, a, b):
        return a > b
if __name__ == '__main__':
    tool = ComparisonTool()
    val1 = 10
    val2 = 5
    result1 = tool.check_greater(val1, val2)
    print(f"{val1} > {val2}: {result1}")
    val3 = 3
    val4 = 7
    result2 = tool.check_greater(val3, val4)
    print(f"{val3} > {val4}: {result2}")
    val5 = 10
    val6 = 10
    result3 = tool.check_greater(val5, val6)
    print(f"{val5} > {val6}: {result3}")