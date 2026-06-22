def calculate_operations(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    division_result = a // b
    return sum_result, difference_result, product_result, division_result

if __name__ == '__main__':
    sample_a = 10
    sample_b = 3
    results = calculate_operations(sample_a, sample_b)
    print("Sum:", results[0])
    print("Difference:", results[1])
    print("Product:", results[2])
    print("Integer Division:", results[3])