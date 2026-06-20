import operator

def evaluate_operation(num1, num2, op):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod
    }
    return operations[op](num1, num2)

if __name__ == '__main__':
    result = evaluate_operation(10, 5, '+')
    print(result)