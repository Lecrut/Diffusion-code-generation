import re

def evaluate_boolean_expression(expression):
    precedence = {'and': 2, 'or': 1}
    
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == 'and':
            values.append(left and right)
        elif operator == 'or':
            values.append(left or right)
    
    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]
    
    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
        elif expression[i:i+3] in ['and', 'or']:
            while (operators and operators[-1] != '(' and
                   greater_precedence(operators[-1], expression[i:i+3])):
                apply_operator(operators, values)
            operators.append(expression[i:i+3])
            i += 2
        else:
            j = i + 1
            while j < len(expression) and expression[j].isalnum():
                j += 1
            values.append(expression[i:j] == 'True')
            i = j - 1
        i += 1
    
    while operators:
        apply_operator(operators, values)
    
    return values[0]

if __name__ == '__main__':
    expression = "True and False or True"
    print(evaluate_boolean_expression(expression))