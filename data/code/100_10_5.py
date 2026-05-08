import re
def is_valid_boolean_expression(expression):
    if not isinstance(expression, str):
        return False
    if not expression:
        return False
    balance = 0
    for char in expression:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    if balance != 0:
        return False
    valid_chars = "()+-*/&|"
    if not all(char in valid_chars or char.isspace() for char in expression):
        return False
    return True
if __name__ == '__main__':
    test_expressions = [
        "true",
        "false",
        "(true && false)",
        "!(true)",
        "true || false",
        "true && (false || true)",
        "true &&",
        "false || )",
        "((true)",
        "true $ false"
    ]
    for expr in test_expressions:
        result = is_valid_boolean_expression(expr)
        print(f"Expression: '{expr}' -> Valid: {result}")
    print("-" * 20)
    invalid_tests = [
        "",
        "true &&",
        "false || )",
        "((true",
        "true $ false"
    ]
    for expr in invalid_tests:
        result = is_valid_boolean_expression(expr)
        print(f"Expression: '{expr}' -> Valid: {result}")