def perform_arithmetic(a, b, c):
    results = {}
    results['addition'] = a + b
    results['subtraction'] = a - b
    results['multiplication'] = a * b
    try:
        results['division'] = a / b
    except ZeroDivisionError:
        results['division'] = "Error: Division by zero"
    return results
if __name__ == '__main__':
    num1 = 10
    num2 = 2
    num3 = 5
    output = perform_arithmetic(num1, num2, num3)
    print(output)