def evaluate_expression(expression):
    return eval(expression)

if __name__ == '__main__':
    expr = "3 * (4 + 2) - 5 / 2"
    result = evaluate_expression(expr)
    print(f"Expression: {expr}")
    print(f"Result of the expression evaluation: {result}")