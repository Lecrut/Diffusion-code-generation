import re
def is_expression_positive(expression: str) -> bool:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return isinstance(result, (int, float)) and result > 0
    except Exception:
        return False
if __name__ == '__main__':
    test_cases = [
        "2 + 3",
        "-5 * -1",
        "(10) / 4",
        "sqrt(9)",                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        "1 + 2",
    ]
    safe_exprs = [
        "2 + 3",
        "-1 * -4",
        "(16) ** 0.5",                                                     
        "True",                                                                                                                                                       
    ]
    for expr in safe_exprs:
        print(f"Expression: {expr} -> Positive: {is_expression_positive(expr)}")