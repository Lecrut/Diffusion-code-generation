def calculate_operations(num1, num2):
    try:
        n1 = float(num1)
        n2 = float(num2)
        sum_val = n1 + n2
        difference_val = n1 - n2
        product_val = n1 * n2
        if n2 != 0:
            quotient_val = n1 / n2
        else:
            quotient_val = "Undefined"
        return sum_val, difference_val, product_val, quotient_val
    except ValueError:
        return "Error: Invalid input. Please enter numeric values.", None, None, None
    except Exception as e:
        return f"An unexpected error occurred: {e}", None, None, None
if __name__ == '__main__':
    sample_num1 = "20"
    sample_num2 = "5"
    sum_result, diff_result, prod_result, quot_result = calculate_operations(sample_num1, sample_num2)
    print(f"Number 1: {sample_num1}")
    print(f"Number 2: {sample_num2}")
    if isinstance(sum_result, str):
        print(sum_result)
    else:
        print(f"Sum: {sum_result}")
        print(f"Difference: {diff_result}")
        print(f"Product: {prod_result}")
        print(f"Quotient: {quot_result}")