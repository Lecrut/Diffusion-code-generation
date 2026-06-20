import operator

def evaluate_operation(num1, num2, operation):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod,
        '//': operator.floordiv
    }
    return operations[operation](num1, num2)

def main():
    sample_num1 = 15
    sample_num2 = 4
    operation = '+'
    result_add = evaluate_operation(sample_num1, sample_num2, operation)
    print("Result of addition:", result_add)
    
    operation = '*'
    result_mul = evaluate_operation(sample_num1, sample_num2, operation)
    print("Result of multiplication:", result_mul)

if __name__ == '__main__':
    main()