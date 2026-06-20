import re

def evaluate_boolean_expression(expression):
    precedence = {'and': 2, 'or': 1}
    operators = set(precedence.keys())
    
    def apply_operator(operators_stack, values_stack):
        operator = operators_stack.pop()
        right = values_stack.pop()
        left = values_stack.pop()
        if operator == 'and':
            values_stack.append(left and right)
        elif operator == 'or':
            values_stack.append(left or right)
    
    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]
    
    expression = re.sub(r'\s+', '', expression)
    tokens = re.findall(r'\b(?:and|or)\b|\(|\)|true|false', expression)
    operators_stack = []
    values_stack = []
    
    for token in tokens:
        if token == 'true':
            values_stack.append(True)
        elif token == 'false':
            values_stack.append(False)
        elif token == '(':
            operators_stack.append(token)
        elif token == ')':
            while operators_stack and operators_stack[-1] != '(':
                apply_operator(operators_stack, values_stack)
            operators_stack.pop()
        else:
            while (operators_stack and operators_stack[-1] != '(' and
                   greater_precedence(operators_stack[-1], token)):
                apply_operator(operators_stack, values_stack)
            operators_stack.append(token)
    
    while operators_stack:
        apply_operator(operators_stack, values_stack)
    
    return values_stack[0]

if __name__ == '__main__':
    print(evaluate_boolean_expression('true and false or true'))