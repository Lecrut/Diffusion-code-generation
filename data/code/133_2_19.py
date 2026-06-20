import ast

class BooleanEvaluator:
    @staticmethod
    def evaluate(expression: str) -> bool:
        return eval(compile(ast.parse(expression).body[0], filename="<ast>", mode="eval"))

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.evaluate("True"))
    print(evaluator.evaluate("False"))
    print(evaluator.evaluate("1 == 1"))
    print(evaluator.evaluate("2 > 3"))