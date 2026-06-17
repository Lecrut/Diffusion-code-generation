import sys
def calculate_operations(num1, num2):
    try:
        sum_result = num1 + num2
        difference_result = num1 - num2
        product_result = num1 * num2
        quotient_result = num1 / num2
        return sum_result, difference_result, product_result, quotient_result
    except ZeroDivisionError:
        return None, None, None, "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input types. Please enter numbers.", None, None, None
if __name__ == '__main__':
    number1 = 20
    number2 = 5
    print(f"First number: {number1}")
    print(f"Second number: {number2}")
    sum_val, diff_val, prod_val, quot_val = calculate_operations(number1, number2)
    if sum_val is not None and diff_val is not None and prod_val is not None and quot_val != "Error: Division by zero is not allowed.":
        print("\n--- Results ---")
        print(f"Sum: {sum_val}")
        print(f"Difference: {diff_val}")
        print(f"Product: {prod_val}")
        print(f"Quotient: {quot_val}")
    else:
        print("\nCalculation failed due to an error.")