def evaluate_expression(expression, inputs):
    stack = []
    for char in expression:
        if char == 'T':
            stack.append(True)
        elif char == 'F':
            stack.append(False)
        elif char == '!':
            stack[-1] = not stack[-1]
        elif char == '&':
            stack.append(stack.pop() and stack.pop())
        elif char == '|':
            stack.append(stack.pop() or stack.pop())
    return stack[0]

def are_equivalent(expression1, expression2):
    inputs = ['TT', 'TF', 'FT', 'FF']
    for input_str in inputs:
        if evaluate_expression(expression1, input_str) != evaluate_expression(expression2, input_str):
            return False
    return True

if __name__ == '__main__':
    expr1 = "T&T"
    expr2 = "F|F"
    print(are_equivalent(expr1, expr2))