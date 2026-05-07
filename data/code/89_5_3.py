import operator
def evaluate_operation(op_symbol, a, b):
    op_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow
    }
    if op_symbol in op_map:
        return op_map[op_symbol](a, b)
    else:
        raise ValueError(f"Unsupported operation: {op_symbol}")
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    op1 = '+'
    result1 = evaluate_operation(op1, num1, num2)
    print(f"Result of {num1} {op1} {num2}: {result1}")
    num3 = 20
    num4 = 4
    op2 = '*'
    result2 = evaluate_operation(op2, num3, num4)
    print(f"Result of {num3} {op2} {num4}: {result2}")
    num5 = 16
    num6 = 2
    op3 = '/'
    result3 = evaluate_operation(op3, num5, num6)
    print(f"Result of {num5} {op3} {num6}: {result3}")
    num7 = 3
    num8 = 4
    op4 = '**'
    result4 = evaluate_operation(op4, num7, num8)
    print(f"Result of {num7} {op4} {num8}: {result4}")