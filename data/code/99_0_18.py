import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '**': operator.pow
}

def evaluate_expression(expression):
    tokens = expression.split()
    stack_values = []
    stack_operators = []

    for token in tokens:
        if token.isdigit():
            stack_values.append(int(token))
        elif token in OPERATORS:
            while (stack_operators and 
                   stack_operators[-1] != '(' and 
                   OPERATORS[token].__priority__ <= OPERATORS[stack_operators[-1]].__priority__):
                right = stack_values.pop()
                left = stack_values.pop()
                operator_func = OPERATORS[stack_operators.pop()]
                result = operator_func(left, right)
                stack_values.append(result)
            stack_operators.append(token)
        elif token == '(':
            stack_operators.append(token)
        elif token == ')':
            while stack_operators[-1] != '(':
                right = stack_values.pop()
                left = stack_values.pop()
                operator_func = OPERATORS[stack_operators.pop()]
                result = operator_func(left, right)
                stack_values.append(result)
            stack_operators.pop()

    while stack_operators:
        right = stack_values.pop()
        left = stack_values.pop()
        operator_func = OPERATORS[stack_operators.pop()]
        result = operator_func(left, right)
        stack_values.append(result)

    return stack_values[0]

if __name__ == '__main__':
    expression = "3 + 5 * (2 - 8) ** 2"
    result = evaluate_expression(expression)
    print(f"Expression: {expression}")
    print(f"Result: {result}")