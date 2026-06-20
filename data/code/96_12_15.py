class BooleanEvaluator:
    TRUE = True
    FALSE = False

    def evaluate_expression(self, expression: str) -> bool:
        try:
            return eval(expression)
        except (SyntaxError, NameError):
            return self.FALSE
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    sample_expression_1 = 'True and False or True'
    print(evaluator.evaluate_expression(sample_expression_1))