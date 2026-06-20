class ExpressionEvaluator:
    SAMPLE_VALUES = [0, 1, -1, 2, -2, 3.14, -3.14]

    @staticmethod
    def evaluate_expression(expr):
        return eval(expr)

    @classmethod
    def verify_equivalence(cls, a_expr, b_expr):
        for value in cls.SAMPLE_VALUES:
            if not cls.evaluate_expression(a_expr) == cls.evaluate_expression(b_expr):
                return False
        return True
if __name__ == '__main__':
    expr1 = 'x ** 2'
    expr2 = 'x * x'
    print(ExpressionEvaluator.verify_equivalence(expr1, expr2))