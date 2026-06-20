class LogicEvaluator:
    def evaluate_expression(self, expr):
        return eval(expr)

    def are_equivalent(self, expr1, expr2):
        value1 = self.evaluate_expression(expr1)
        value2 = self.evaluate_expression(expr2)
        return value1 == value2

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    expr_a = "True"
    expr_b = "True"
    print(f"Are {expr_a} and {expr_b} equivalent? {evaluator.are_equivalent(expr_a, expr_b)}")
    expr_c = "True"
    expr_d = "False"
    print(f"Are {expr_c} and {expr_d} equivalent? {evaluator.are_equivalent(expr_c, expr_d)}")
    expr_e = "False"
    expr_f = "False"
    print(f"Are {expr_e} and {expr_f} equivalent? {evaluator.are_equivalent(expr_e, expr_f)}")