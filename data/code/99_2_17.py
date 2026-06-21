def evaluate_expressions(expressions):
    results = []
    precedence_map = {
        '**': 3,
        '*': 2,
        '/': 2,
        '//': 2,
        '%': 2,
        '+': 1,
        '-': 1
    }
    for expr in expressions:
        if not isinstance(expr, str):
            raise ValueError(f"Expected string, got {type(expr).__name__}")
        if not expr.strip():
            raise ValueError("Empty expression")
        try:
            val = eval(expr)
            tokens = expr.split()
            steps = []
            for token in tokens:
                if token in precedence_map:
                    steps.append(f"Operator '{token}' (precedence {precedence_map[token]})")
                elif token.replace('.', '', 1).isdigit():
                    steps.append(f"Operand '{token}'")
                elif token == '(':
                    steps.append("Parenthesis '('")
                elif token == ')':
                    steps.append("Parenthesis ')'")
            results.append((expr, val, steps))
        except Exception as e:
            results.append((expr, None, [f"Error: {str(e)}"]))
    return results

if __name__ == '__main__':
    sample_expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "2 ** 3 ** 2",
        "10 / 3 + 1",
        "10 // 3 + 1",
        "True and False or True",
        "1 + 2 + 3 * 4 ** 2",
        "5 * (3 + 2) - 1"
    ]
    output = evaluate_expressions(sample_expressions)
    print(output)