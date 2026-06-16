def calculate_operations(num1, num2):
    try:
        result_sum = num1 + num2
        result_difference = num1 - num2
        result_product = num1 * num2
        if num2 != 0:
            result_quotient = num1 / num2
        else:
            result_quotient = "Undefined (Division by zero)"
        return result_sum, result_difference, result_product, result_quotient
    except TypeError:
        return "Error: Inputs must be numeric.", None, None, None
    except Exception as e:
        return f"An unexpected error occurred: {e}", None, None, None
if __name__ == '__main__':
    input1 = 20
    input2 = 5
    sum_val, diff_val, prod_val, quot_val = calculate_operations(input1, input2)
    print(f"Input Numbers: {input1}, {input2}")
    print(f"Sum: {sum_val}")
    print(f"Difference: {diff_val}")
    print(f"Product: {prod_val}")
    print(f"Quotient: {quot_val}")
    input3 = "hello"
    input4 = 10
    sum_val, diff_val, prod_val, quot_val = calculate_operations(input3, input4)
    print(f"\nInput Numbers: {input3}, {input4}")
    print(f"Sum: {sum_val}")
    print(f"Difference: {diff_val}")
    print(f"Product: {prod_val}")
    print(f"Quotient: {quot_val}")
    input5 = 10
    input6 = 0
    sum_val, diff_val, prod_val, quot_val = calculate_operations(input5, input6)
    print(f"\nInput Numbers: {input5}, {input6}")
    print(f"Sum: {sum_val}")
    print(f"Difference: {diff_val}")
    print(f"Product: {prod_val}")
    print(f"Quotient: {quot_val}")