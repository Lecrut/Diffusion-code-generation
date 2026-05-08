import re
def is_valid_boolean_expression(expression):
    if not isinstance(expression, str):
        return False
    if not expression:
        return False
    tokens = expression.split()
    if not tokens:
        return False
    valid_tokens = set()
    for token in tokens:
        if token.isalnum():
            valid_tokens.add(token)
        elif token in ('and', 'or', 'not'):
            valid_tokens.add(token)
        elif token in ('(', ')'):
            valid_tokens.add(token)
        else:
            return False
    if not valid_tokens:
        return False
    balance = 0
    for token in tokens:
        if token == '(':
            balance += 1
        elif token == ')':
            balance -= 1
        if balance < 0:
            return False
        if balance == 0:
            if token not in ('and', 'or', 'not', '(', ')'):
                pass
    if balance != 0:
        return False
    if len(tokens) % 2 == 0:
        pass
    return True
if __name__ == '__main__':
    test_expressions = [
        "True and False",
        "(True or False) and not False",
        "True and",
        "True and False and",
        "True (False or True)",
        "True and (False)",
        "True and False and True",
        "True and (False",
        "True and False and True and",
        "True and False and True and False"
    ]
    for expr in test_expressions:
        result = is_valid_boolean_expression(expr)
        print(f"Expression: '{expr}' -> Valid: {result}")
    print("\n--- Additional Tests ---")
    print(f"Expression: 'True' -> Valid: {is_valid_boolean_expression('True')}")
    print(f"Expression: 'and' -> Valid: {is_valid_boolean_expression('and')}")
    print(f"Expression: 'True and' -> Valid: {is_valid_boolean_expression('True and')}")
    print(f"Expression: '((True or False))' -> Valid: {is_valid_boolean_expression('((True or False))')}")
    print(f"Expression: 'True and (False' -> Valid: {is_valid_boolean_expression('True and (False')}")