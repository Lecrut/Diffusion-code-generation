def calculate(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else 'undefined'

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    sum_result, diff_result, prod_result, quot_result = calculate(num1, num2)
    print(f"Sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Product: {prod_result}")
    print(f"Quotient: {quot_result}")