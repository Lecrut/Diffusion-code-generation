def evaluate_expression(expression, inputs):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            sub_expr = ''
            while stack[-1] != '(':
                sub_expr = stack.pop() + sub_expr
            stack.pop()
            stack.append(evaluate_expression(sub_expr, inputs))
        elif char == 'T' or char == 'F':
            stack.append(char)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if char == '&':
                result = 'T' if op1 == 'T' and op2 == 'T' else 'F'
            elif char == '|':
                result = 'T' if op1 == 'T' or op2 == 'T' else 'F'
            elif char == '^':
                result = 'T' if op1 != op2 else 'F'
            stack.append(result)
    return stack[0]

def are_equivalent(expression1, expression2):
    inputs = ['T', 'F']
    truth_table1 = {input_val: evaluate_expression(expression1, input_val) for input_val in inputs}
    truth_table2 = {input_val: evaluate_expression(expression2, input_val) for input_val in inputs}
    return truth_table1 == truth_table2

if __name__ == '__main__':
    expression1 = 'T & (F | T)'
    expression2 = '(T & F) | T'
    print(are_equivalent(expression1, expression2))