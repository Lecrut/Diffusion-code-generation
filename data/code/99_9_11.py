from operator import and_, or_

NOT_PRECEDENCE = 3
AND_PRECEDENCE = 2
OR_PRECEDENCE = 1

def evaluate_expression(expr):
    stack_values = []
    stack_operators = []

    def apply_operator():
        operator = stack_operators.pop()
        right = stack_values.pop()
        left = stack_values.pop()
        if operator == 'NOT':
            stack_values.append(not right)
        elif operator == 'AND':
            stack_values.append(and_(left, right))
        elif operator == 'OR':
            stack_values.append(or_(left, right))

    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue

        if expr[i] in ['NOT', 'AND', 'OR']:
            precedence = NOT_PRECEDENCE if expr[i] == 'NOT' else AND_PRECEDENCE if expr[i] == 'AND' else OR_PRECEDENCE
            while stack_operators and precedence <= stack_precedence[stack_operators[-1]]:
                apply_operator()
            stack_operators.append(expr[i])
        elif expr[i].isalpha():
            j = i + 1
            while j < len(expr) and expr[j].isalnum() or expr[j] == '_':
                j += 1
            token = expr[i:j]
            if token == 'True' or token == 'False':
                stack_values.append(token == 'True')
            else:
                raise ValueError(f"Invalid token: {token}")
            i = j - 1
        elif expr[i] == '(':
            stack_operators.append(expr[i])
        elif expr[i] == ')':
            while stack_operators and stack_operators[-1] != '(':
                apply_operator()
            if not stack_operators or stack_operators[-1] != '(':
                raise ValueError("Unmatched parentheses")
            stack_operators.pop()

        i += 1

    while stack_operators:
        apply_operator()

    return stack_values[0]

if __name__ == '__main__':
    expression = "(True AND False) OR (NOT True)"
    result = evaluate_expression(expression)
    print(result)