class BooleanExpression:
    def __init__(self, expression):
        self.expression = expression
    def evaluate(self, variables):
        if not self.expression:
            return False
        tokens = self.expression.split()
        result = []
        for token in tokens:
            if token == 'AND':
                result.append('AND')
            elif token == 'OR':
                result.append('OR')
            elif token == 'NOT':
                if len(result) > 0:
                    result.append('NOT')
                else:
                    result.append('NOT')
            elif token in variables:
                result.append(variables[token])
            else:
                raise ValueError(f"Unknown token: {token}")
        return self._evaluate_tokens(result)
    def _evaluate_tokens(self, tokens):
        if not tokens:
            return False
        if len(tokens) == 1:
            if tokens[0] == 'True':
                return True
            if tokens[0] == 'False':
                return False
            raise ValueError("Invalid single token")
        if tokens[0] == 'NOT':
            if len(tokens) < 2:
                raise ValueError("NOT requires an operand")
            operand = self._evaluate_tokens(tokens[1:])
            return not operand
        if tokens[0] == 'AND' or tokens[0] == 'OR':
            if len(tokens) < 3:
                raise ValueError("Binary operator requires two operands")
            left_operand = self._evaluate_tokens(tokens[1:-1])
            operator = tokens[1]
            right_operand = self._evaluate_tokens(tokens[-1])
            if operator == 'AND':
                return left_operand and right_operand
            elif operator == 'OR':
                return left_operand or right_operand
            else:
                raise ValueError(f"Unknown operator: {operator}")
        if isinstance(tokens[0], bool):
            return tokens[0]
        raise ValueError("Evaluation error")
def test_expression(expression_str, variables):
    try:
        expr = BooleanExpression(expression_str)
        result = expr.evaluate(variables)
        return result
    except Exception as e:
        return f"Error: {e}"
if __name__ == '__main__':
    test_cases = [
        ("True", {"A": True}),
        ("False", {"A": False}),
        ("NOT True", {"A": True}),
        ("NOT False", {"A": False}),
        ("NOT NOT True", {"A": True}),
        ("A AND True", {"A": True}),
        ("True AND False", {"A": True, "B": False}),
        ("A OR False", {"A": True}),
        ("A OR B", {"A": True, "B": True}),
        ("NOT A AND B", {"A": True, "B": True}),
        ("NOT (A OR B)", {"A": True, "B": True}),
        ("A AND (B OR NOT A)", {"A": True, "B": False}),
        ("A AND (NOT B)", {"A": True, "B": False}),
        ("NOT (A AND B)", {"A": True, "B": True}),
        ("A OR (NOT B)", {"A": True, "B": False}),
        ("NOT (A OR B)", {"A": False, "B": False}),
    ]
    for expr_str, vars_dict in test_cases:
        result = test_expression(expr_str, vars_dict)
        print(f"Expression: '{expr_str}' with variables {vars_dict}: {result}")