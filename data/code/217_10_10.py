def perform_arithmetic_operations(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be integers or floats.")
    
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    
    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "Undefined"
    
    return sum_result, difference_result, product_result, quotient_result

if __name__ == '__main__':
    num1 = 20
    num2 = 5
    results = perform_arithmetic_operations(num1, num2)
    print("--- Arithmetic Operations ---")
    print(f"First Number: {num1}")
    print(f"Second Number: {num2}")
    print("-" * 30)
    print(f"Sum: {num1} + {num2} = {results[0]}")
    print(f"Difference: {num1} - {num2} = {results[1]}")
    print(f"Product: {num1} * {num2} = {results[2]}")
    if results[3] != "Undefined":
        print(f"Quotient: {num1} / {num2} = {results[3]}")
    else:
        print(f"Quotient: {num1} / {num2} = {results[3]}")