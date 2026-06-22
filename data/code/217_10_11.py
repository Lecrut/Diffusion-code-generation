def calculate_operations(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else 'Undefined'
    return sum_result, difference_result, product_result, quotient_result

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    results = calculate_operations(num1, num2)
    print(f"Sum: {results[0]}")
    print(f"Difference: {results[1]}")
    print(f"Product: {results[2]}")
    print(f"Quotient: {results[3]}")