def perform_operations(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    division_result = None if b == 0 else a / b
    modulus_result = None if b == 0 else a % b
    return sum_result, difference_result, product_result, division_result, modulus_result

if __name__ == '__main__':
    sample_a = 15
    sample_b = 4
    results = perform_operations(sample_a, sample_b)
    print(results)