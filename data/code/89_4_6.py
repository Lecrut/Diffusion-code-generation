import operator

def evaluate_operation(num1, num2, op):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod,
        '//': operator.floordiv
    }
    return ops[op](num1, num2)

if __name__ == '__main__':
    result = evaluate_operation(10, 5, '+')
    print(result)