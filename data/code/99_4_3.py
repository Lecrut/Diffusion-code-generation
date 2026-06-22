def evaluate_parenthesized_expression(expression: str) -> float:
    if not expression:
        raise ValueError("Empty expression")
    expression = expression.strip()
    if not expression:
        raise ValueError("Empty expression")
    
    if expression.startswith('(') and expression.endswith(')'):
        inner = expression[1:-1].strip()
        if not inner:
            raise ValueError("Empty parentheses")
        return evaluate_parenthesized_expression(inner)
    
    if not _is_number(expression):
        raise ValueError(f"Invalid expression: {expression}")
    
    return float(expression)

def _is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    print(evaluate_parenthesized_expression("((10 + 5) * (2 - 1))"))
    print(evaluate_parenthesized_expression("((10.5 + 5.5) * (2.0 - 1.0))"))
    print(evaluate_parenthesized_expression("42"))
    print(evaluate_parenthesized_expression("((3 + 4) * (5 + 6))"))
    print(evaluate_parenthesized_expression("((100 / 10) + (50 - 25))"))