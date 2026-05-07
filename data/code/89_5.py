import operator
def evaluate_operation(op, a, b):
    return op(a, b)
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    addition_result = evaluate_operation(operator.add, num1, num2)
    multiplication_result = evaluate_operation(operator.mul, num1, num2)
    division_result = evaluate_operation(operator.truediv, num1, num2)
    floor_division_result = evaluate_operation(operator.floordiv, num1, num2)
    modulo_result = evaluate_operation(operator.mod, num1, num2)
    print(f"Addition of {num1} and {num2}: {addition_result}")
    print(f"Multiplication of {num1} and {num2}: {multiplication_result}")
    print(f"True division of {num1} by {num2}: {division_result}")
    print(f"Floor division of {num1} by {num2}: {floor_division_result}")
    print(f"Modulo of {num1} by {num2}: {modulo_result}")