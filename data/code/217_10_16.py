def calculate_operations(num1, num2):
    operations = {
        'sum': num1 + num2,
        'difference': num1 - num2,
        'product': num1 * num2,
        'quotient': num1 / num2 if num2 != 0 else "Undefined"
    }
    return operations

if __name__ == '__main__':
    num1 = 20
    num2 = 5
    results = calculate_operations(num1, num2)
    print("--- Arithmetic Operations ---")
    print(f"First Number: {num1}")
    print(f"Second Number: {num2}")
    print("-" * 30)
    for operation, result in results.items():
        print(f"{operation.capitalize()}: {result}")