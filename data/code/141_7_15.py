class ExpressionEvaluator:

    def evaluate(self, expression):
        return eval(expression)
if __name__ == '__main__':
    evaluator = ExpressionEvaluator()
    expression_and = '5 & 3'
    expression_not = '~7'
    expression_or = f'({expression_and}) | ({expression_not})'
    result_and = evaluator.evaluate(expression_and)
    result_not = evaluator.evaluate(expression_not)
    result_or = evaluator.evaluate(expression_or)
    print(result_and)
    print(result_not)
    print(result_or)