import operator

def execute_math_operation(first_number, second_number, operation_symbol):
    math_operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod,
        '//': operator.floordiv
    }
    return math_operations[operation_symbol](first_number, second_number)

if __name__ == '__main__':
    sample_num1 = 7
    sample_num2 = 3
    symbol = '+'
    result = execute_math_operation(sample_num1, sample_num2, symbol)
    print(result)