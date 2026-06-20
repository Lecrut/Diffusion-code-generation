x = 12
y = 3

def calculate_operations(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b
    modulus_result = a % b
    return sum_result, difference_result, product_result, quotient_result, modulus_result

if __name__ == '__main__':
    results = calculate_operations(x, y)
    print(f"Sum: {results[0]}, Difference: {results[1]}, Product: {results[2]}, Quotient: {results[3]:.2f}, Modulus: {results[4]}")