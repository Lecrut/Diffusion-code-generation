class ComparisonTool:
    def check_greater(self, value1, value2):
        if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
            return value1 > value2
        return NotImplemented
if __name__ == '__main__':
    tool = ComparisonTool()
    v1 = 1000000000
    v2 = 500000000
    result1 = tool.check_greater(v1, v2)
    print(f"Comparing {v1} and {v2}: {result1}")
    v3 = -500
    v4 = -1000
    result2 = tool.check_greater(v3, v4)
    print(f"Comparing {v3} and {v4}: {result2}")
    v5 = 3.14159e10
    v6 = 3.14159e10 + 1.0
    result3 = tool.check_greater(v5, v6)
    print(f"Comparing {v5} and {v6}: {result3}")
    large_v1 = 999999999999999999
    large_v2 = 1000000000000000000
    result4 = tool.check_greater(large_v1, large_v2)
    print(f"Comparing large numbers: {result4}")
    result5 = tool.check_greater(10, "hello")
    print(f"Comparing 10 and 'hello': {result5}")