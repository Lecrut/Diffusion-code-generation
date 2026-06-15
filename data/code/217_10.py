def calculate_operations():
    num1 = 20
    num2 = 5
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2 if num2 != 0 else "Undefined"
    print("--- Arithmetic Operations ---")
    print(f"First Number: {num1}")
    print(f"Second Number: {num2}")
    print("-" * 30)
    print(f"Sum: {num1} + {num2} = {sum_result}")
    print(f"Difference: {num1} - {num2} = {difference_result}")
    print(f"Product: {num1} * {num2} = {product_result}")
    if isinstance(quotient_result, (int, float)):
        print(f"Quotient: {num1} / {num2} = {quotient_result}")
    else:
        print(f"Quotient: {num1} / {num2} = {quotient_result}")
if __name__ == '__main__':
    calculate_operations()