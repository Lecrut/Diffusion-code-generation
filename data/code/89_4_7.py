import operator

def evaluate_expression(num1, num2, op):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod,
        '//': operator.floordiv
    }
    return operations[op](num1, num2)

if __name__ == '__main__':
    sample_num1 = 8
    sample_num2 = 3
    operation = '+'
    result = evaluate_expression(sample_num1, sample_num2, operation)
    print(result)