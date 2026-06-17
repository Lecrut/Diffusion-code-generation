def calculate_operations(num1, num2):
    try:
        sum_val = num1 + num2
        diff_val = num1 - num2
        prod_val = num1 * num2
        quot_val = num1 / num2
        return sum_val, diff_val, prod_val, quot_val
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed.", None, None, None
    except TypeError:
        return "Error: Invalid input types provided.", None, None, None
if __name__ == '__main__':
    num1 = 20
    num2 = 5
    sum_result, diff_result, prod_result, quot_result = calculate_operations(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Product: {prod_result}")
    print(f"Quotient: {quot_result}")