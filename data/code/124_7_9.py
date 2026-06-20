def calculate_operations(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both x and y must be numbers.")
    
    sum_result = x + y
    difference_result = x - y
    product_result = x * y
    quotient_result = x / y if y != 0 else None
    modulus_result = x % y if y != 0 else None
    
    return sum_result, difference_result, product_result, quotient_result, modulus_result

if __name__ == '__main__':
    x = 12
    y = 3
    results = calculate_operations(x, y)
    print(f"Sum: {results[0]}, Difference: {results[1]}, Product: {results[2]}, Quotient: {results[3]}, Modulus: {results[4]}")