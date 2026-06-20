def evaluate_expression(expression):
    return eval(expression)

if __name__ == '__main__':
    sample_expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "5 + 6 / 2 - 1",
        "10 / 2 + 5 * 3",
        "8 - 2 * 3 + 4",
        "True and False or True",
        "not (3 == 3)"
    ]
    
    for expr in sample_expressions:
        print(f"Expression: {expr} -> Result: {evaluate_expression(expr)}")