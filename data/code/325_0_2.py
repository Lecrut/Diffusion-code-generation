def calculate_operations(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot perform division by zero.")
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2
    return sum_result, difference_result, product_result, quotient_result
if __name__ == '__main__':
    try:
        input_num1 = 20
        input_num2 = 5
        if not isinstance(input_num1, (int, float)) or not isinstance(input_num2, (int, float)):
            raise ValueError("Input must be numeric.")
        sum_val, diff_val, prod_val, quot_val = calculate_operations(input_num1, input_num2)
        print(f"Number 1: {input_num1}")
        print(f"Number 2: {input_num2}")
        print(f"Sum: {sum_val}")
        print(f"Difference: {diff_val}")
        print(f"Product: {prod_val}")
        print(f"Quotient: {quot_val}")
    except ValueError as e:
        print(f"Error: Invalid input provided. {e}")
    except ZeroDivisionError as e:
        print(f"Error: Calculation failed due to division by zero. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")