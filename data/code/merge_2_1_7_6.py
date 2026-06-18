import re
def evaluate_expression(expression: str) -> bool:
    if not expression.strip():
        return False
    try:
        result = eval(expression)
        return isinstance(result, (int, float)) and result > 0
    except Exception:
        return False
if __name__ == '__main__':
    test_cases = [
        "2 + 3",
        "-5 * -1",
        "(10 / 2) + 4",
        "sqrt(-4)",
        "not a valid expression",
        "",
        "True"
    ]
    for expr in test_cases:
        print(f"{expr!r} -> {evaluate_expression(expr)}")