NUM1 = 25
NUM2 = 10

def calculate_operations(a=NUM1, b=NUM2):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    division_result = a // b
    
    return sum_result, difference_result, product_result, division_result

if __name__ == '__main__':
    results = calculate_operations()
    print(f"Sum: {results[0]}")
    print(f"Difference: {results[1]}")
    print(f"Product: {results[2]}")
    print(f"Integer Division: {results[3]}")