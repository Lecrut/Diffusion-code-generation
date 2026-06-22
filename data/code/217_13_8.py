def calculate_operations(a, b):
    return a + b, a - b, a * b, a // b

if __name__ == '__main__':
    x = 10
    y = 3
    sum_result, diff_result, product_result, div_result = calculate_operations(x, y)
    print(f"Sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Product: {product_result}")
    print(f"Integer Division: {div_result}")