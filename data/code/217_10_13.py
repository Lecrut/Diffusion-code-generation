def perform_operations(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2 if num2 != 0 else "Undefined"
    return sum_result, difference_result, product_result, quotient_result

def main():
    num1 = 20
    num2 = 5
    results = perform_operations(num1, num2)
    print("--- Arithmetic Operations ---")
    print(f"First Number: {num1}")
    print(f"Second Number: {num2}")
    print("-" * 30)
    print(f"Sum: {results[0]}")
    print(f"Difference: {results[1]}")
    print(f"Product: {results[2]}")
    if isinstance(results[3], (int, float)):
        print(f"Quotient: {results[3]}")
    else:
        print(f"Quotient: {results[3]}")

if __name__ == '__main__':
    main()