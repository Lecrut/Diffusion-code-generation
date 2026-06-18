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
        "1 + 2 * 3",
    ]
    safe_pattern = re.compile(r'^[\d\+\-\*\/\(\)\.\s]+$')
    for expr in test_cases:
        if not safe_pattern.match(expr):
            print(f"Invalid syntax detected for: {expr}")
            continue
        is_positive = evaluate_expression(expr)
        status = "Positive" if is_positive else "Non-positive or Error"
        print(f"{expr} -> {status}")