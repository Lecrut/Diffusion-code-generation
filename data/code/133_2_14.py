import ast

class BooleanEvaluator:
    TRUE = True
    FALSE = False
    
    @staticmethod
    def evaluate_expression(expression: str) -> bool:
        return eval(compile(ast.parse(expression).body[0], filename="<ast>", mode="eval"))

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.evaluate_expression("True"))
    print(evaluator.evaluate_expression("False"))
    print(evaluator.evaluate_expression("1 == 1"))
    print(evaluator.evaluate_expression("2 > 3"))