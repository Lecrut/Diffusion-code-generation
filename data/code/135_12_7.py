class LogicChecker:
    def are_equivalent(self, expr1, expr2):
        if expr1 == expr2:
            return True
        return not (expr1 ^ expr2)
if __name__ == '__main__':
    checker = LogicChecker()
    expr_a = True
    expr_b = True
    print(f"Are {expr_a} and {expr_b} equivalent? {checker.are_equivalent(expr_a, expr_b)}")
    expr_c = True
    expr_d = False
    print(f"Are {expr_c} and {expr_d} equivalent? {checker.are_equivalent(expr_c, expr_d)}")
    expr_e = True
    expr_f = False
    print(f"Are {expr_e} and {expr_f} equivalent? {checker.are_equivalent(expr_e, expr_f)}")
    expr_g = False
    expr_h = False
    print(f"Are {expr_g} and {expr_h} equivalent? {checker.are_equivalent(expr_g, expr_h)}")
    expr_i = True
    expr_j = True
    print(f"Are {expr_i} and {expr_j} equivalent? {checker.are_equivalent(expr_i, expr_j)}")