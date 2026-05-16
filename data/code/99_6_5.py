def setup_operator_precedence():
    precedence_map = {
        '(': 0,
        ')': 0,
        '|': 1,
        '&': 2,
        '==': 3,
        '!=': 3,
        '>': 4,
        '<': 4,
        '+': 5,
        '-': 5,
        '*': 6,
        '/': 6,
        'not': 7
    }
    return precedence_map
def evaluate_expression(expression, precedence_map):
    tokens = expression.split()
    if not tokens:
        return None
    result_stack = []
    operator_stack = []
    def apply_op(op, values):
        if len(values) < 2:
            raise ValueError("Insufficient operands for operator " + op)
        right = values.pop()
        left = values.pop()
        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '*':
            values.append(left * right)
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            values.append(left / right)
        elif op == '==':
            values.append(left == right)
        elif op == '!=':
            values.append(left != right)
        elif op == '>':
            values.append(left > right)
        elif op == '<':
            values.append(left < right)
        elif op == '&':
            values.append(left and right)
        elif op == '|':
            values.append(left or right)
        elif op == 'not':
            values.append(not left)
        else:
            raise ValueError("Unknown operator: " + op)
        values.append(values)
    for token in tokens:
        if token in precedence_map:
            op_precedence = precedence_map[token]
            if token in '()':
                if token == '(':
                    operator_stack.append(token)
                elif token == ')':
                    while operator_stack and operator_stack[-1] != '(':
                        op = operator_stack.pop()
                        apply_op(op, result_stack)
                    if not operator_stack or operator_stack[-1] != '(':
                        raise ValueError("Mismatched parentheses")
                    operator_stack.pop()
                continue
            if token == 'not':
                if len(result_stack) < 1:
                    raise ValueError("Not enough operands for 'not'")
                operand = result_stack.pop()
                result_stack.append(not operand)
                continue
            while (operator_stack and operator_stack[-1] != '(' and 
                   precedence_map.get(operator_stack[-1], -1) >= op_precedence):
                op = operator_stack.pop()
                apply_op(op, result_stack)
            operator_stack.append(token)
        else:
            try:
                value = float(token)
                result_stack.append(value)
            except ValueError:
                raise ValueError(f"Invalid token encountered: {token}")
    while operator_stack:
        op = operator_stack.pop()
        if op == '(':
            raise ValueError("Mismatched parentheses")
        apply_op(op, result_stack)
    if len(result_stack) != 1:
        raise ValueError("Invalid expression structure")
    return result_stack[0]
if __name__ == '__main__':
    operator_precedence = setup_operator_precedence()
    expression1 = "10 + 5 * 2"
    expression2 = "(10 + 5) * 2"
    expression3 = "not (10 > 5 & 3 < 8)"
    expression4 = "10 / 2 + 3"
    print(f"Expression 1: {expression1}")
    try:
        result1 = evaluate_expression(expression1, operator_precedence)
        print(f"Result 1: {result1}\n")
    except Exception as e:
        print(f"Error evaluating Expression 1: {e}\n")
    print(f"Expression 2: {expression2}")
    try:
        result2 = evaluate_expression(expression2, operator_precedence)
        print(f"Result 2: {result2}\n")
    except Exception as e:
        print(f"Error evaluating Expression 2: {e}\n")
    print(f"Expression 3: {expression3}")
    try:
        result3 = evaluate_expression(expression3, operator_precedence)
        print(f"Result 3: {result3}\n")
    except Exception as e:
        print(f"Error evaluating Expression 3: {e}\n")
    print(f"Expression 4: {expression4}")
    try:
        result4 = evaluate_expression(expression4, operator_precedence)
        print(f"Result 4: {result4}\n")
    except Exception as e:
        print(f"Error evaluating Expression 4: {e}\n")