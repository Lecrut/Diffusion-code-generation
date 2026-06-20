import re

def evaluate_boolean_expression(expression):
    operators = {'and': 2, 'or': 1}
    tokens = re.findall('\\b\\w+\\b|\\(|\\)', expression)

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == 'and':
            values.append(left and right)
        elif operator == 'or':
            values.append(left or right)
        return values

    def greater_precedence(op1, op2):
        return operators[op1] > operators[op2]
    output = []
    ops = []
    for token in tokens:
        if token.isdigit():
            output.append(int(token))
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                output = apply_operator(ops, output)
            ops.pop()
        else:
            while ops and ops[-1] != '(' and greater_precedence(ops[-1], token):
                output = apply_operator(ops, output)
            ops.append(token)
    while ops:
        output = apply_operator(ops, output)
    return output[0]
if __name__ == '__main__':
    expression = 'True or False and True'
    result = evaluate_boolean_expression(expression)
    print(result)