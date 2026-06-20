import re

def evaluate_boolean_expression(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    operators = set(precedence.keys())

    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

    def evaluate(tokens):
        values = []
        operators = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if isinstance(token, int):
                values.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()
            else:
                while operators and operators[-1] in operators and greater_precedence(operators[-1], token):
                    apply_operator(operators, values)
                operators.append(token)
            i += 1
        while operators:
            apply_operator(operators, values)
        return values[0]
    tokens = re.findall('\\d+|\\+|-|\\*|/', expression)
    result = evaluate(tokens)
    return result
if __name__ == '__main__':
    sample_expression = '3 + 5 * (2 - 8)'
    print(evaluate_boolean_expression(sample_expression))