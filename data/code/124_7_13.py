x = 12
y = 3

def calculate_operations(a, b):
    return a + b, a - b, a * b, a / b, a % b

if __name__ == '__main__':
    sum_result, diff_result, prod_result, quot_result, mod_result = calculate_operations(x, y)
    print(f"Sum: {sum_result}, Difference: {diff_result}, Product: {prod_result}, Quotient: {quot_result}, Modulus: {mod_result}")