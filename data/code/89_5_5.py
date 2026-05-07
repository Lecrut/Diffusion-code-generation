import operator
def evaluate_operation(op, a, b):
    return op(a, b)
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    addition = evaluate_operation(operator.add, num1, num2)
    subtraction = evaluate_operation(operator.sub, num1, num2)
    multiplication = evaluate_operation(operator.mul, num1, num2)
    division = evaluate_operation(operator.truediv, num1, num2)
    floor_division = evaluate_operation(operator.floordiv, num1, num2)
    print(f"10 + 5 = {addition}")
    print(f"10 - 5 = {subtraction}")
    print(f"10 * 5 = {multiplication}")
    print(f"10 / 5 = {division}")
    print(f"10 // 5 = {floor_division}")