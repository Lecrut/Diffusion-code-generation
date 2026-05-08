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
        return self._evaluate_tokens(result, variables)
    def _evaluate_tokens(self, tokens, variables):
        if not tokens:
            return False
        if len(tokens) == 1:
            if tokens[0] == 'True':
                return True
            elif tokens[0] == 'False':
                return False
            else:
                raise ValueError(f"Invalid single token: {tokens[0]}")
        if tokens[0] == 'NOT':
            operand = tokens[1]
            if operand not in variables:
                raise ValueError(f"Variable not found: {operand}")
            return not variables[operand]
        if tokens[0] == 'AND' or tokens[0] == 'OR':
            if len(tokens) < 3:
                raise ValueError("Malformed boolean expression structure")
            left_operand = tokens[1]
            right_operand = tokens[2]
            left_val = self._evaluate_tokens([left_operand], variables)
            right_val = self._evaluate_tokens([right_operand], variables)
            if tokens[0] == 'AND':
                return left_val and right_val
            elif tokens[0] == 'OR':
                return left_val or right_val
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
        ("NOT A", {"A": True}),
        ("NOT False", {"A": False}),
        ("A AND True", {"A": True}),
        ("True OR A", {"A": True}),
        ("A AND NOT A", {"A": True}),
        ("NOT (A OR B)", {"A": True, "B": False}),
        ("A AND (B OR C)", {"A": True, "B": True, "C": False}),
        ("NOT (A AND B)", {"A": True, "B": True}),
        ("A OR (B AND C)", {"A": True, "B": True, "C": True}),
    ]
    print("--- Testing Nested Boolean Logic Framework ---")
    for expr_str, vars_dict in test_cases:
        result = test_expression(expr_str, vars_dict)
        print(f"Expression: '{expr_str}' with variables {vars_dict}: Result = {result}")
        print("-" * 20)