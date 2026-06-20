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
        input_dict = {'T': True, 'F': False}
        values1 = [input_dict[input_str[i]] for i in range(2)]
        values2 = [input_dict[input_str[i+2]] for i in range(2)]
        if evaluate_expression(expression1, values1) != evaluate_expression(expression2, values2):
            return False
    return True

if __name__ == '__main__':
    expression1 = 'T&T'
    expression2 = 'F|F'
    print(are_equivalent(expression1, expression2))