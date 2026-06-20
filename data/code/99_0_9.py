def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

if __name__ == '__main__':
    expr = "3 + 5 * (2 - 8) ** 2"
    result = evaluate_expression(expr)
    print(f"Evaluation of '{expr}': {result}")