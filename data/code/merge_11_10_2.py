import sys
def calculate_operations(num1, num2):
    try:
        n1 = float(num1)
        n2 = float(num2)
        sum_result = n1 + n2
        difference_result = n1 - n2
        product_result = n1 * n2
        quotient_result = n1 / n2 if n2 != 0 else "Undefined (Division by zero)"
        return sum_result, difference_result, product_result, quotient_result
    except ValueError:
        return None, None, None, "Error: Invalid input. Please enter numeric values."
    except ZeroDivisionError:
        return None, None, None, "Error: Division by zero is not allowed."
if __name__ == '__main__':
    sample_num1 = "20"
    sample_num2 = "5"
    sum_val, diff_val, prod_val, quot_val = calculate_operations(sample_num1, sample_num2)
    print(f"Number 1: {sample_num1}")
    print(f"Number 2: {sample_num2}")
    if sum_val is not None:
        print(f"Sum: {sum_val}")
        print(f"Difference: {diff_val}")
        print(f"Product: {prod_val}")
        print(f"Quotient: {quot_val}")
    else:
        print(quot_val)