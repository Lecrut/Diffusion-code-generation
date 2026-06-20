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
    sample_num1 = 4
    sample_num2 = 3
    operation = '*'
    result = evaluate_operation(sample_num1, sample_num2, operation)
    print(result)