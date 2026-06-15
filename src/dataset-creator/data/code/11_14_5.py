def perform_operations(num1, num2):
    print(f"\n--- Performing operations on {num1} and {num2} ---")
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
        print(f"Division: Cannot divide by zero.")
if __name__ == '__main__':
    number1 = 15
    number2 = 4
    perform_operations(number1, number2)