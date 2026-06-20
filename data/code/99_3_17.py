def evaluate_boolean_expression(expression):
    return eval(expression)

if __name__ == '__main__':
    TRUE = True
    FALSE = False
    
    sample_expressions = [
        "TRUE and FALSE",
        "TRUE or FALSE",
        "not TRUE",
        "10 > 5",
        "3 < 2",
        "5 == 5",
        "True != False"
    ]
    
    for expr in sample_expressions:
        result = evaluate_boolean_expression(expr)
        print(f"{expr} evaluates to: {result}")