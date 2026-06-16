def calculate_operations(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot perform division by zero.")
    sum_val = num1 + num2
    difference_val = num1 - num2
    product_val = num1 * num2
    quotient_val = num1 / num2
    return sum_val, difference_val, product_val, quotient_val
if __name__ == '__main__':
    try:
        input_num1 = 15
        input_num2 = 5
        result_sum, result_diff, result_prod, result_quot = calculate_operations(input_num1, input_num2)
        print(f"First number: {input_num1}")
        print(f"Second number: {input_num2}")
        print(f"Sum: {result_sum}")
        print(f"Difference: {result_diff}")
        print(f"Product: {result_prod}")
        print(f"Quotient: {result_quot}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")