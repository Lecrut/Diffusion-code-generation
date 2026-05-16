class ComparisonTool:
    def check_greater(self, value1, value2):
        if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
            return value1 > value2
        return NotImplemented
if __name__ == '__main__':
    tool = ComparisonTool()
    v1 = 1000000000000000000
    v2 = 500000000000000000
    result1 = tool.check_greater(v1, v2)
    print(f"Comparing {v1} and {v2}: {result1}")
    v3 = 10
    v4 = 20
    result2 = tool.check_greater(v3, v4)
    print(f"Comparing {v3} and {v4}: {result2}")
    v5 = 5.5e18
    v6 = 5.5e18
    result3 = tool.check_greater(v5, v6)
    print(f"Comparing {v5} and {v6}: {result3}")
    v7 = 999999999999999999
    v8 = 1000000000000000000
    result4 = tool.check_greater(v7, v8)
    print(f"Comparing {v7} and {v8}: {result4}")
    v9 = 100
    v10 = "text"
    result5 = tool.check_greater(v9, v10)
    print(f"Comparing {v9} and {v10}: {result5}")