class ComparisonTool:
    def check_greater(self, value1, value2):
        return value1 > value2
if __name__ == '__main__':
    tool = ComparisonTool()
    v1_int = 1000000000
    v2_int = 500000000
    result_int = tool.check_greater(v1_int, v2_int)
    print(f"Comparing {v1_int} and {v2_int}: {result_int}")
    v1_float = 1.23456789e20
    v2_float = 1.23456788e20
    result_float = tool.check_greater(v1_float, v2_float)
    print(f"Comparing {v1_float} and {v2_float}: {result_float}")
    v1_neg = -5000000000000000000
    v2_neg = -6000000000000000000
    result_neg = tool.check_greater(v1_neg, v2_neg)
    print(f"Comparing {v1_neg} and {v2_neg}: {result_neg}")
    v1_eq = 12345
    v2_eq = 12345
    result_eq = tool.check_greater(v1_eq, v2_eq)
    print(f"Comparing {v1_eq} and {v2_eq}: {result_eq}")