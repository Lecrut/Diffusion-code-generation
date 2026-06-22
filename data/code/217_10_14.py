def calculate_operations(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b
    quotient = a / b if b != 0 else 'Undefined'
    return sum_result, difference, product, quotient

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result = calculate_operations(num1, num2)
    print(f"Sum: {result[0]}")
    print(f"Difference: {result[1]}")
    print(f"Product: {result[2]}")
    print(f"Quotient: {result[3]}")