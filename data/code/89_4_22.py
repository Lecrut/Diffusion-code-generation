import operator
OPERATIONS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow, '%': operator.mod, '//': operator.floordiv}

def evaluate_operation(num1, num2, operation):
    return OPERATIONS[operation](num1, num2)
if __name__ == '__main__':
    sample_num1 = 10
    sample_num2 = 5
    operation = '+'
    result = evaluate_operation(sample_num1, sample_num2, operation)
    print(result)