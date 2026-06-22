def calculate_operations(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    if b != 0:
        division_result = a // b
    else:
        division_result = None
    return sum_result, difference_result, product_result, division_result

if __name__ == '__main__':
    num1 = 25
    num2 = 4
    result_sum, result_diff, result_prod, result_div = calculate_operations(num1, num2)
    print(f"Sum: {result_sum}")
    print(f"Difference: {result_diff}")
    print(f"Product: {result_prod}")
    if result_div is not None:
        print(f"Integer Division: {result_div}")
    else:
        print("Integer Division by zero")