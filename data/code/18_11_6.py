class ComparisonTool:
    def check_greater(self, value1, value2):
        return value1 > value2
if __name__ == '__main__':
    tool = ComparisonTool()
    large_val1 = 10**18
    large_val2 = 10**18 + 1
    result1 = tool.check_greater(large_val1, large_val2)
    print(f"Comparing {large_val1} and {large_val2}: {result1}")
    large_val3 = 5000000000000000000
    large_val4 = 4999999999999999999
    result2 = tool.check_greater(large_val3, large_val4)
    print(f"Comparing {large_val3} and {large_val4}: {result2}")
    small_val1 = 5
    small_val2 = 3
    result3 = tool.check_greater(small_val1, small_val2)
    print(f"Comparing {small_val1} and {small_val2}: {result3}")