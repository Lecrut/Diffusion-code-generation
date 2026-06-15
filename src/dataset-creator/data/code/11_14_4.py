def perform_operations(num1, num2):
    print("\n--- Performing Operations ---")
    print(f"First number: {num1}")
    print(f"Second number: {num2}")
    sum_result = num1 + num2
    print(f"Addition ({num1} + {num2}): {sum_result}")
    diff_result = num1 - num2
    print(f"Subtraction ({num1} - {num2}): {diff_result}")
    prod_result = num1 * num2
    print(f"Multiplication ({num1} * {num2}): {prod_result}")
    if num2 != 0:
        div_result = num1 / num2
        print(f"Division ({num1} / {num2}): {div_result}")
    else:
        print(f"Division ({num1} / {num2}): Cannot divide by zero")
if __name__ == '__main__':
    a = 20
    b = 5
    perform_operations(a, b)