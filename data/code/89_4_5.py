import operator

def evaluate_operation(num1, num2, operation):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod,
        '//': operator.floordiv
    }
    return ops[operation](num1, num2)

if __name__ == '__main__':
    result = evaluate_operation(10, 5, '+')
    print(result)