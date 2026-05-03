class ComparisonTool:
    def check_greater(self, value1, value2):
        return value1 > value2
if __name__ == '__main__':
    tool = ComparisonTool()
    v1_int = 1000000000
    v2_int = 500000000
    result_int = tool.check_greater(v1_int, v2_int)
    print(f"Comparing {v1_int} and {v2_int}: {result_int}")
    v1_large = 999999999999999999
    v2_large = 1000000000000000000
    result_large = tool.check_greater(v1_large, v2_large)
    print(f"Comparing {v1_large} and {v2_large}: {result_large}")
    v1_neg = -500
    v2_neg = -100
    result_neg = tool.check_greater(v1_neg, v2_neg)
    print(f"Comparing {v1_neg} and {v2_neg}: {result_neg}")
    v1_eq = 42
    v2_eq = 42
    result_eq = tool.check_greater(v1_eq, v2_eq)
    print(f"Comparing {v1_eq} and {v2_eq}: {result_eq}")