import re
def evaluate_expression(expression: str) -> bool:
    if not expression.strip():
        return False
    pattern = r'^[\d\+\-\*\/\.eE\s]+$'
    if not re.match(pattern, expression):
        raise ValueError("Invalid characters in expression")
    try:
        result = eval(expression)
    except ZeroDivisionError:
        raise ValueError("Division by zero detected")
    except Exception as e:
        raise RuntimeError(f"Expression evaluation failed: {e}") from e
    return result > 0
if __name__ == '__main__':
    test_cases = [
        "2 + 3",
        "(1 - 5) / (4 - 6)",
        "**invalid syntax**",
        "sqrt(9)",
        "-(-5)"
    ]
    for expr in test_cases:
        try:
            is_positive = evaluate_expression(expr)
            print(f"{expr} -> {is_positive}")
        except Exception as e:
            print(f"Error evaluating '{expr}': {e}")