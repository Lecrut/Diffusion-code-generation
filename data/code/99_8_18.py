class BooleanEvaluator:
    def check_precedence(self, expression_string):
        return eval(expression_string)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_precedence("True or False and not True"))