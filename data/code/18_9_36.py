class ComparisonTool:

    def check_greater(self, value1, value2):
        comparison_cache = {(value1, value2): None, (value2, value1): None}
        if comparison_cache[value1, value2] is not None:
            return comparison_cache[value1, value2]
        result = value1 > value2
        comparison_cache[value1, value2] = result
        comparison_cache[value2, value1] = not result
        return result
if __name__ == '__main__':
    tool = ComparisonTool()
    result1 = tool.check_greater(10 ** 1000, 999 ** 999)
    print(result1)
    result2 = tool.check_greater(10 ** 18, 10 ** 17)
    print(result2)
    result3 = tool.check_greater(10 ** 1000, 999 ** 1000)
    print(result3)
    result4 = tool.check_greater(10 ** 10000, 999999999999999999)
    print(result4)