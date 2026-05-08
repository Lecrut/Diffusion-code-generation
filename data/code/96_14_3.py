import operator
def evaluate_nested_boolean_expression(expression):
    stack = []
    operators = {
        'and': operator.and_,
        'or': operator.or_,
        'not': operator.not_,
        '==': operator.eq,
        '!=': operator.ne,
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le
    }
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.append(float(token))
        elif token in operators:
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                op = stack.pop()
                right = stack.pop()
                stack.append(operators[op](right))
            if not stack or stack[-1] != '(':
                raise ValueError("Mismatched parentheses")
            stack.pop()
        else:
            try:
                value = float(token)
                stack.append(value)
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Malformed expression")
if __name__ == '__main__':
    expressions = [
        "True and (False or True)",
        "not (1 == 1)",
        "(5 > 3) and (10 < 20)",
        "True or (False and False)",
        "not (5 > 10)",
        "True and (5 > 3) or False"
    ]
    for expr in expressions:
        try:
            result = evaluate_nested_boolean_expression(expr)
            print(f"Expression: {expr}")
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Expression: {expr}")
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Expression: {expr}")
            print(f"Unexpected Error: {e}\n")