class LogicChecker:
    def are_equivalent(self, expr1, expr2):
        return expr1 == expr2
if __name__ == '__main__':
    checker = LogicChecker()
    expr_a = (True and False) or False
    expr_b = False
    expr_c = False
    print(f"expr_a: {expr_a}")
    print(f"expr_b: {expr_b}")
    print(f"expr_c: {expr_c}")
    result1 = checker.are_equivalent(expr_a, expr_b)
    print(f"Are expr_a and expr_b equivalent? {result1}")
    result2 = checker.are_equivalent(expr_a, expr_c)
    print(f"Are expr_a and expr_c equivalent? {result2}")
    expr_d = True
    expr_e = True
    result3 = checker.are_equivalent(expr_d, expr_e)
    print(f"Are expr_d and expr_e equivalent? {result3}")