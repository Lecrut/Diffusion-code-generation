def perform_arithmetic_operations(num1: int, num2: int) -> dict:
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2 if num2 != 0 else "Undefined"
    
    return {
        'sum': sum_result,
        'difference': difference_result,
        'product': product_result,
        'quotient': quotient_result
    }

if __name__ == '__main__':
    sample_num1, sample_num2 = 30, 7
    results = perform_arithmetic_operations(sample_num1, sample_num2)
    
    print("--- Arithmetic Operations ---")
    print(f"First Number: {sample_num1}")
    print(f"Second Number: {sample_num2}")
    print("-" * 30)
    print(f"Sum: {sample_num1} + {sample_num2} = {results['sum']}")
    print(f"Difference: {sample_num1} - {sample_num2} = {results['difference']}")
    print(f"Product: {sample_num1} * {sample_num2} = {results['product']}")
    if results['quotient'] != "Undefined":
        print(f"Quotient: {sample_num1} / {sample_num2} = {results['quotient']}")
    else:
        print(f"Quotient: {sample_num1} / {sample_num2} = {results['quotient']}")