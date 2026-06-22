def calculate_operations(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b
    quotient = a / b if b != 0 else None
    return sum_result, difference, product, quotient

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result = calculate_operations(num1, num2)
    print("Sum:", result[0])
    print("Difference:", result[1])
    print("Product:", result[2])
    print("Quotient:", result[3] if result[3] is not None else "Division by zero")