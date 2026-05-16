def calculate_operations(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    sum_val = num1 + num2
    difference_val = num1 - num2
    product_val = num1 * num2
    quotient_val = num1 / num2
    return sum_val, difference_val, product_val, quotient_val
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    try:
        sum_result, diff_result, prod_result, quot_result = calculate_operations(num1, num2)
        print(f"Number 1: {num1}")
        print(f"Number 2: {num2}")
        print(f"Sum: {sum_result}")
        print(f"Difference: {diff_result}")
        print(f"Product: {prod_result}")
        print(f"Quotient: {quot_result}")
    except ValueError as e:
        print(f"Error: {e}")