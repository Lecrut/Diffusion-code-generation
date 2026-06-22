class BooleanExpressionEvaluator:
    def __init__(self, expression):
        self.expression = expression

    def _evaluate(self, node):
        if isinstance(node, bool):
            return node
        if isinstance(node, (int, float)):
            return bool(node)
        if not isinstance(node, list):
            raise ValueError(f"Unsupported node type: {type(node)}")
        if len(node) == 0:
            raise ValueError("Empty expression list")
        if len(node) == 1:
            return self._evaluate(node[0])
        
        operator = node[1]
        left_val = self._evaluate(node[0])
        right_val = self._evaluate(node[2]) if len(node) > 2 else None

        if operator == 'AND':
            return left_val and right_val
        if operator == 'OR':
            return left_val or right_val
        if operator == 'NOT':
            return not left_val
        if operator == 'XOR':
            return left_val ^ right_val
        if operator == 'NAND':
            return not (left_val and right_val)
        if operator == 'NOR':
            return not (left_val or right_val)
        
        raise ValueError(f"Unsupported operator: {operator}")

    def evaluate(self):
        return self._evaluate(self.expression)

if __name__ == '__main__':
    expr1 = [['A', 'AND', 'B'], 'AND', 'C']
    evaluator1 = BooleanExpressionEvaluator(expr1)
    print(evaluator1.evaluate())

    expr2 = ['A', 'OR', ['B', 'AND', 'C']]
    evaluator2 = BooleanExpressionEvaluator(expr2)
    print(evaluator2.evaluate())

    expr3 = ['A', 'NOT', ['B', 'XOR', 'C']]
    evaluator3 = BooleanExpressionEvaluator(expr3)
    print(evaluator3.evaluate())

    expr4 = [['A', 'AND', 'B'], 'OR', ['C', 'NAND', 'D']]
    evaluator4 = BooleanExpressionEvaluator(expr4)
    print(evaluator4.evaluate())

    expr5 = ['A', 'NOR', ['B', 'OR', 'C']]
    evaluator5 = BooleanExpressionEvaluator(expr5)
    print(evaluator5.evaluate())

    expr6 = ['A', 'XOR', ['B', 'AND', 'C']]
    evaluator6 = BooleanExpressionEvaluator(expr6)
    print(evaluator6.evaluate())

    expr7 = ['A', 'AND', ['B', 'OR', ['C', 'AND', 'D']]]
    evaluator7 = BooleanExpressionEvaluator(expr7)
    print(evaluator7.evaluate())

    expr8 = [['A', 'OR', 'B'], 'AND', ['C', 'OR', 'D']]
    evaluator8 = BooleanExpressionEvaluator(expr8)
    print(evaluator8.evaluate())

    expr9 = ['A', 'AND', 'B']
    evaluator9 = BooleanExpressionEvaluator(expr9)
    print(evaluator9.evaluate())

    expr10 = ['A', 'OR', 'B']
    evaluator10 = BooleanExpressionEvaluator(expr10)
    print(evaluator10.evaluate())