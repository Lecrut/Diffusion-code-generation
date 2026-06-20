def evaluate_boolean_expression(expr):
    return eval(expr)

if __name__ == '__main__':
    expressions = {
        "2 > 1 and 3 < 4": True,
        "5 <= 6 or 7 != 8": True,
        "not False and True": True,
        "10 % 2 == 0": True,
        "(9 / 3) ** 2 < 10": True
    }
    
    for expr, expected in expressions.items():
        result = evaluate_boolean_expression(expr)
        print(f"Expression: {expr}, Expected: {expected}, Result: {result}")