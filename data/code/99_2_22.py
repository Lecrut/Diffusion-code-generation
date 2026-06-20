import operator

def evaluate_expressions(expressions):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow, '%': operator.mod, '//': operator.floordiv}
    results = []
    for expr in expressions:
        tokens = expr.split()
        stack = []
        operators = []
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token in ops:
                while operators and ops[token].__name__ != '(' and (ops[operators[-1]].__name__ >= ops[token].__name__):
                    b = stack.pop()
                    a = stack.pop()
                    operator_func = ops[operators.pop()]
                    result = operator_func(a, b)
                    stack.append(result)
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators[-1] != '(':
                    b = stack.pop()
                    a = stack.pop()
                    operator_func = ops[operators.pop()]
                    result = operator_func(a, b)
                    stack.append(result)
                operators.pop()
        while operators:
            b = stack.pop()
            a = stack.pop()
            operator_func = ops[operators.pop()]
            result = operator_func(a, b)
            stack.append(result)
        results.append(stack[0])
    return results
if __name__ == '__main__':
    expressions = ['3 + 5 * 2', '(7 - 4) / 3', '10 ** 2 % 3', '8 // 3']
    print(evaluate_expressions(expressions))