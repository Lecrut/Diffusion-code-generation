def perform_operations(num1, num2):
    print(f"First number: {num1}")
    print(f"Second number: {num2}")
    print("\n--- Arithmetic Operations ---")
    sum_result = num1 + num2
    print(f"Addition ({num1} + {num2}): {sum_result}")
    difference_result = num1 - num2
    print(f"Subtraction ({num1} - {num2}): {difference_result}")
    product_result = num1 * num2
    print(f"Multiplication ({num1} * {num2}): {product_result}")
    if num2 != 0:
        quotient_result = num1 / num2
        print(f"Division ({num1} / {num2}): {quotient_result}")
    else:
        print(f"Division ({num1} / {num2}): Cannot divide by zero")
if __name__ == '__main__':
    number1 = 15
    number2 = 4
    perform_operations(number1, number2)