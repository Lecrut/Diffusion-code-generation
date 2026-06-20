def calculate_operations(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else None
    modulus_result = a % b if b != 0 else None
    return sum_result, difference_result, product_result, quotient_result, modulus_result

if __name__ == '__main__':
    x = 12
    y = 3
    results = calculate_operations(x, y)
    print(f"Sum: {results[0]}, Difference: {results[1]}, Product: {results[2]}, Quotient: {results[3]}, Modulus: {results[4]}")