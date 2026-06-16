import re
def evaluate_expression(expression: str) -> bool:
    try:
        result = eval(expression)
        return isinstance(result, (int, float)) and result > 0
    except Exception:
        return False
if __name__ == '__main__':
    test_cases = [
        "2 + 3",
        "-5 * -1",
        "(10 / 2) - 4",
        "sqrt(9)",                                                                        
        "a + b" if False else None,                                                          
    ]
    expressions = ["3 * 5", "-10 / 2", "(4 - 8) + 6", "not a number"]
    for expr in expressions:
        print(f"{expr} -> {evaluate_expression(expr)}")