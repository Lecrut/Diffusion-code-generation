def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
if __name__ == '__main__':
    a = 10
    b = 5
    op1 = '+'
    result1 = calculator(a, b, op1)
    print(f"{a} {op1} {b} = {result1}")
    a = 20
    b = 4
    op2 = '-'
    result2 = calculator(a, b, op2)
    print(f"{a} {op2} {b} = {result2}")
    a = 6
    b = 7
    op3 = '*'
    result3 = calculator(a, b, op3)
    print(f"{a} {op3} {b} = {result3}")
    a = 15
    b = 3
    op4 = '/'
    result4 = calculator(a, b, op4)
    print(f"{a} {op4} {b} = {result4}")
    a = 10
    b = 0
    op5 = '/'
    result5 = calculator(a, b, op5)
    print(f"{a} {op5} {b} = {result5}")
    a = 10
    b = '%'
    op6 = '%'
    result6 = calculator(a, b, op6)
    print(f"{a} {op6} {b} = {result6}")