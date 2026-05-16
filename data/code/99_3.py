import operator
def evaluate_expression_with_precedence(expressions):
    results = []
    for expr in expressions:
        tokens = expr.split()
        if not tokens:
            results.append(None)
            continue
        parsed_tokens = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                parsed_tokens.append(float(token))
            elif token in "+-*/^()":
                parsed_tokens.append(token)
            else:
                raise ValueError(f"Invalid token in expression: {token}")
        if not parsed_tokens:
            results.append(None)
            continue
        def apply_op(op, b, a):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                return a / b
            if op == '^': return a ** b
            raise ValueError(f"Unknown operator: {op}")
        def evaluate_tokens(tokens):
            values = []
            ops = []
            i = 0
            while i < len(tokens):
                token = tokens[i]
                if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                    values.append(float(token))
                elif token in "+-*/^":
                    ops.append(token)
                i += 1
            if not values:
                return None
            result = values[0]
            op_index = 0
            for i in range(1, len(ops)):
                op = ops[i-1]
                val2 = values[i]
                val1 = result
                if op == '(':
                    pass
                elif op == '(':
                    pass
                elif op == '(':
                    pass
                elif op == '(':
                    pass
                if op in "+-*/^":
                    result = apply_op(op, val2, val1)
                ops.pop()
                values.append(result)
            return values[0] if values else None
        try:
            result = eval(expr)
            results.append(result)
        except Exception as e:
            results.append(f"Error: {e}")
    return results
if __name__ == '__main__':
    sample_expressions = [
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "10 / 2 - 3 * 5",
        "2^3 - 1",
        "5 + 6 * (7 - 8)"
    ]
    print("--- Evaluating Expressions with Python's Operator Precedence ---")
    for expr in sample_expressions:
        print(f"\nExpression: {expr}")
        try:
            result = eval(expr)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Evaluation Error: {e}")
        print("---")