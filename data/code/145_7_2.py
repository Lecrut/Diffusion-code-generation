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
            operand = tokens[1]
            if operand == 'True':
                return False
            if operand == 'False':
                return True
            raise ValueError("Invalid operand after NOT")
        if tokens[0] == 'AND' or tokens[0] == 'OR':
            if len(tokens) < 3:
                raise ValueError("Incomplete boolean operation")
            left_operand = tokens[1]
            right_operand = tokens[2]
            left_val = self._evaluate_tokens([left_operand])
            right_val = self._evaluate_tokens([right_operand])
            if tokens[0] == 'AND':
                return left_val and right_val
            elif tokens[0] == 'OR':
                return left_val or right_val
        raise ValueError("Evaluation error")
def test_nested_logic(expression_str, variables):
    try:
        expr = BooleanExpression(expression_str)
        result = expr.evaluate(variables)
        return result
    except Exception as e:
        return f"Error: {e}"
if __name__ == '__main__':
    test_cases = [
        ("True", {"True": True, "False": False}),
        ("False", {"True": True, "False": False}),
        ("NOT True", {"True": True, "False": False}),
        ("NOT False", {"True": True, "False": False}),
        ("True AND False", {"True": True, "False": False}),
        ("True OR False", {"True": True, "False": False}),
        ("NOT True AND False", {"True": True, "False": False}),
        ("True OR NOT False", {"True": True, "False": False}),
        ("NOT (True OR False)", {"True": True, "False": False}),
        ("True AND (False OR True)", {"True": True, "False": False}),
        ("NOT (True AND False)", {"True": True, "False": False}),
        ("NOT (True OR False AND True)", {"True": True, "False": False}),
    ]
    for expr_str, vars_map in test_cases:
        result = test_nested_logic(expr_str, vars_map)
        print(f"Expression: '{expr_str}' with variables {vars_map}: {result}")