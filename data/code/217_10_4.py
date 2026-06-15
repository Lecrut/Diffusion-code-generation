def calculate_operations():
    num1 = 20
    num2 = 5
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "Undefined"
    print("--- Arithmetic Operations ---")
    print(f"First Number: {num1}")
    print(f"Second Number: {num2}")
    print("-" * 30)
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")
    print(f"Product: {product_result}")
    if isinstance(quotient_result, (int, float)):
        print(f"Quotient: {quotient_result}")
    else:
        print(f"Quotient: {quotient_result}")
if __name__ == '__main__':
    calculate_operations()