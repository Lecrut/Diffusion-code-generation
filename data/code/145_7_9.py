class BooleanExpression:
    def __init__(self, expression):
        self.expression = expression
    def evaluate(self, values):
        if not isinstance(self.expression, str):
            raise TypeError("Expression must be a string.")
        sub_expressions = self._split_and_parse(self.expression)
        results = []
        for sub_expr in sub_expressions:
            results.append(self._evaluate_sub_expression(sub_expr, values))
        return results
    def _split_and_parse(self, expression):
        if not expression:
            return []
        tokens = expression.split(' ')
        parsed_structure = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                balance = 1
                start = i + 1
                j = start
                while j < len(tokens) and balance != 0:
                    if tokens[j] == '(':
                        balance += 1
                    elif tokens[j] == ')':
                        balance -= 1
                    j += 1
                if balance == 0:
                    sub_expr = " ".join(tokens[start:j-1])
                    parsed_structure.append(sub_expr)
                    i = j - 1
                else:
                    raise ValueError("Mismatched parentheses in expression.")
            else:
                parsed_structure.append(token)
            i += 1
        return parsed_structure
    def _evaluate_sub_expression(self, sub_expression, values):
        if not sub_expression:
            return None
        if sub_expression.startswith('(') and sub_expression.endswith(')'):
            content = sub_expression[1:-1].strip()
            if not content:
                return None
            sub_tokens = content.split(' ')
            if len(sub_tokens) == 1:
                token = sub_tokens[0]
                if token in values:
                    return values[token]
                else:
                    raise ValueError(f"Undefined variable: {token}")
            if len(sub_tokens) > 1:
                if len(sub_tokens) == 3 and sub_tokens[1] == '==':
                    try:
                        left_val = values.get(sub_tokens[0])
                        right_val = values.get(sub_tokens[2])
                        if left_val is not None and right_val is not None:
                            return left_val == right_val
                        else:
                            raise ValueError("One or both operands undefined.")
                    except Exception:
                        raise ValueError(f"Error evaluating equality: {sub_expression}")
                else:
                    raise ValueError(f"Unsupported structure in nested expression: {sub_expression}")
        else:
            if sub_expression in values:
                return values[sub_expression]
            else:
                raise ValueError(f"Undefined variable: {sub_expression}")
def test_framework(expression_string, input_values):
    try:
        expr = BooleanExpression(expression_string)
        result = expr.evaluate(input_values)
        return result
    except Exception as e:
        return f"ERROR: {e}"
if __name__ == '__main__':
    test_cases = [
        ("A", {"A": True}),
        ("A == A", {"A": True}),
        ("(A == A) and B", {"A": True, "B": False}),
        ("A and (B or C)", {"A": True, "B": False, "C": True}),
        ("not A", {"A": False}),
        ("not (A and B)", {"A": True, "B": True}),
        ("A == B or C", {"A": True, "B": False, "C": True}),
        ("(A == B) and not C", {"A": True, "B": True, "C": False}),
        ("A == B and C == D", {"A": True, "B": True, "C": True, "D": False}),
        ("A and not B", {"A": True, "B": False}),
        ("A == B", {"A": True, "B": True}),
        ("A == B", {"A": True, "B": False}),
    ]
    print("--- Testing Nested Boolean Logic Framework ---")
    for expr_str, values in test_cases:
        result = test_framework(expr_str, values)
        print(f"Expression: '{expr_str}' with values {values}: Result = {result}")
        print("-" * 20)