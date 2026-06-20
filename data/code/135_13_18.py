def evaluate_expression(expression, inputs):
    stack = []
    for char in expression:
        if char == 'T':
            stack.append(True)
        elif char == 'F':
            stack.append(False)
        elif char == '!':
            stack.append(not stack.pop())
        elif char == '&':
            stack.append(stack.pop() and stack.pop())
        elif char == '|':
            stack.append(stack.pop() or stack.pop())
    return stack[0]

def are_equivalent(expression1, expression2):
    inputs = ['T', 'F']
    for i in range(4):
        input_combination = [inputs[i & 1], inputs[i >> 1 & 1]]
        result1 = evaluate_expression(expression1, input_combination)
        result2 = evaluate_expression(expression2, input_combination)
        if result1 != result2:
            return False
    return True
if __name__ == '__main__':
    expression1 = 'T&T'
    expression2 = 'F|F'
    print(are_equivalent(expression1, expression2))