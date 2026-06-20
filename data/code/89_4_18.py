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
    result_add = evaluate_operation(10, 5, '+')
    result_sub = evaluate_operation(10, 5, '-')
    result_mul = evaluate_operation(4, 3, '*')
    result_div = evaluate_operation(8, 2, '/')
    result_pow = evaluate_operation(2, 3, '**')
    result_mod = evaluate_operation(10, 3, '%')
    result_floordiv = evaluate_operation(9, 2, '//')

    print("Addition:", result_add)
    print("Subtraction:", result_sub)
    print("Multiplication:", result_mul)
    print("Division:", result_div)
    print("Power:", result_pow)
    print("Modulus:", result_mod)
    print("Floor Division:", result_floordiv)