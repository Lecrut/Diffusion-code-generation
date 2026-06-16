import re
def evaluate_expression(expression: str) -> bool:
    pattern = r'^[\d\+\-\*\/\.eE\s]+$'
    if not re.match(pattern, expression):
        raise ValueError("Invalid mathematical syntax")
    try:
        result = eval(expression)
        return result > 0
    except ZeroDivisionError:
        return False
if __name__ == '__main__':
    test_cases = [
        "2 + 3",
        "-5 * -1",
        "(10 / 4)",
        "sqrt(9) + 1" if True else None,                                                                             
        "a + b"
    ]
    valid_syntax = [
        "2 + 3",
        "-5 * -1", 
        "(10 / 4)",
        "sqrt(9) + 1",
        "a + b"
    ]
    for expr in ["2+3", "-5*-1", "invalid syntax here", "1/0"]:
        try:
            is_positive = evaluate_expression(expr)
            print(f"{expr} -> {is_positive}")
        except ValueError as e:
            print(f"Error evaluating '{expr}': {e}")