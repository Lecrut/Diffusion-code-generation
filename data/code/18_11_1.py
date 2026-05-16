class ComparisonTool:
    def check_greater(self, value1, value2):
        return value1 > value2
if __name__ == '__main__':
    tool = ComparisonTool()
    v1 = 1000000000
    v2 = 500000000
    result1 = tool.check_greater(v1, v2)
    print(f"Comparing {v1} and {v2}: {result1}")
    v3 = 999999999999999999
    v4 = 1000000000000000000
    result2 = tool.check_greater(v3, v4)
    print(f"Comparing {v3} and {v4}: {result2}")
    v5 = 123456789012345
    v6 = 123456789012344
    result3 = tool.check_greater(v5, v6)
    print(f"Comparing {v5} and {v6}: {result3}")
    v7 = 555
    v8 = 555
    result4 = tool.check_greater(v7, v8)
    print(f"Comparing {v7} and {v8}: {result4}")