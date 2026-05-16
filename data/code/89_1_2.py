def evaluate_binary_op(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
if __name__ == '__main__':
    result1 = evaluate_binary_op(10, 5, '+')
    print(f"10 + 5 = {result1}")
    result2 = evaluate_binary_op(10, 5, '-')
    print(f"10 - 5 = {result2}")
    result3 = evaluate_binary_op(10, 5, '*')
    print(f"10 * 5 = {result3}")
    result4 = evaluate_binary_op(10, 5, '/')
    print(f"10 / 5 = {result4}")
    result5 = evaluate_binary_op(10, 0, '/')
    print(f"10 / 0 = {result5}")
    result6 = evaluate_binary_op(10, 3, '%')
    print(f"10 % 3 = {result6}")