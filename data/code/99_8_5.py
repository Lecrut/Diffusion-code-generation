class BooleanEvaluator:
    def check_precedence(self, expression_string):
        return eval(expression_string)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("True and False or not True"))
    print(evaluator.check_precedence("(3 > 2) and (4 < 5)"))
    print(evaluator.check_precedence("not (10 % 2 == 0)"))