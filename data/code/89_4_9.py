import operator

def validate_operation(operation):
    valid_operations = {'+', '-', '*', '/', '**', '%', '//'}
    if operation not in valid_operations:
        raise ValueError(f"Invalid operation: {operation}. Supported operations are: {valid_operations}")

def evaluate_expression(num1, num2, op):
    validate_operation(op)
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
    sample_num1 = 8
    sample_num2 = 3
    operation = '+'
    result = evaluate_expression(sample_num1, sample_num2, operation)
    print(result)