def evaluate_expressions(expressions):
    results = []
    for expr in expressions:
        if not is_valid_expression(expr):
            raise ValueError(f"Invalid expression: {expr}")
        result = eval(expr)
        results.append((expr, result))
    return results

def is_valid_expression(expression):
    valid_chars = "0123456789+-*/(). "
    for char in expression:
        if char not in valid_chars:
            return False
    try:
        eval(expression)
        return True
    except SyntaxError:
        return False

if __name__ == '__main__':
    sample_expressions = [
        "3 + 4 * 2",
        "(10 / 3) ** 2",
        "5 % 2 + 3",
        "2 ** 3 - 4"
    ]
    print(evaluate_expressions(sample_expressions))