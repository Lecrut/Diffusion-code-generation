import operator
def evaluate_expression_with_precedence(expression):
    tokens = expression.split()
    results = []
    for i in range(len(tokens)):
        token = tokens[i]
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            results.append(float(token))
        elif token in "+-*/^()":
            results.append(token)
        else:
            raise ValueError(f"Invalid token: {token}")
    def apply_op(op, b, a):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': 
            if b == 0: raise ZeroDivisionError
            return a / b
        if op == '^': return a ** b
        raise ValueError(f"Unknown operator: {op}")
    def process_tokens(tokens_list):
        values = []
        ops = []
        for token in tokens_list:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                values.append(float(token))
            elif token in "+-*/^":
                ops.append(token)
            else:
                raise ValueError(f"Invalid token encountered: {token}")
        if not values:
            return None
        if not ops:
            return values[-1]
        temp_values = []
        temp_ops = []
        i = 0
        while i < len(values):
            if values[i] == '^' and len(values) > i + 1 and values[i+1] in (values[i+2] if i+2 < len(values) else []):
                pass
            temp_values.append(values[i])
            i += 1
        if not ops:
            return values[0] if values else None
        temp_values = [values[0]]
        temp_ops = []
        for j in range(len(values)):
            if values[j] in ('+', '-', '*', '/', '^'):
                if values[j] == '^':
                    if len(temp_values) < 2:
                        raise ValueError("Syntax error: Missing operand for exponentiation")
                    op = temp_ops[-1]
                    val2 = temp_values.pop()
                    val1 = temp_values.pop()
                    temp_values.append(apply_op(op, val1, val2))
                else:
                    op = values[j]
                    if len(temp_values) < 2:
                        raise ValueError("Syntax error: Missing operands for binary operator")
                    val2 = temp_values.pop()
                    val1 = temp_values.pop()
                    temp_values.append(apply_op(op, val1, val2))
                    temp_ops.append(op)
            else:
                temp_values.append(float(values[j]))
        if not temp_values:
            return None
        result = temp_values[0]
        for k in range(len(temp_ops)):
            op = temp_ops[k]
            val2 = temp_values.pop()
            val1 = temp_values.pop()
            result = apply_op(op, val1, val2)
            temp_values.append(result)
        return result
    return process_tokens(tokens)
if __name__ == '__main__':
    expressions = [
        "10 + 5 * 2",
        "3 + 4 * 2 / 3",
        "2^3 * 4",
        "100 / 5 + 20",
        "8 + 2 * 3^2"
    ]
    for expr in expressions:
        print(f"Expression: {expr}")
        try:
            result = evaluate_expression_with_precedence(expr)
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error evaluating {expr}: {e}\n")