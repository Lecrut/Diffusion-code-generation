def perform_operations(num1, num2):
    print("\n--- Performing Operations ---")
    sum_result = num1 + num2
    print(f"Addition: {num1} + {num2} = {sum_result}")
    diff_result = num1 - num2
    print(f"Subtraction: {num1} - {num2} = {diff_result}")
    prod_result = num1 * num2
    print(f"Multiplication: {num1} * {num2} = {prod_result}")
    if num2 != 0:
        quotient_result = num1 / num2
        print(f"Division: {num1} / {num2} = {quotient_result}")
    else:
        print("Division: Cannot divide by zero.")
if __name__ == '__main__':
    a = 15
    b = 4
    print(f"Sample Numbers Selected: First number is {a}, Second number is {b}")
    perform_operations(a, b)