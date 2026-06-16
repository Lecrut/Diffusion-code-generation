def calculate_operations(num1, num2):
    try:
        sum_result = num1 + num2
        difference_result = num1 - num2
        product_result = num1 * num2
        quotient_result = num1 / num2
        return sum_result, difference_result, product_result, quotient_result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed.", None, None, None
    except TypeError:
        return "Error: Invalid input types provided.", None, None, None
if __name__ == '__main__':
    num1 = 20
    num2 = 5
    sum_val, diff_val, prod_val, quot_val = calculate_operations(num1, num2)
    if isinstance(sum_val, str):
        print(sum_val)
    else:
        print(f"Number 1: {num1}")
        print(f"Number 2: {num2}")
        print(f"Sum: {sum_val}")
        print(f"Difference: {diff_val}")
        print(f"Product: {prod_val}")
        print(f"Quotient: {quot_val}")