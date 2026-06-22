def perform_arithmetic_operations(num1: int, num2: int) -> dict:
    operations = {
        "sum": num1 + num2,
        "difference": num1 - num2,
        "product": num1 * num2,
        "quotient": num1 / num2 if num2 != 0 else "Undefined"
    }
    return operations

if __name__ == '__main__':
    sample_values = {"num1": 20, "num2": 5}
    results = perform_arithmetic_operations(sample_values["num1"], sample_values["num2"])
    print("--- Arithmetic Operations ---")
    for operation, result in results.items():
        print(f"{operation.capitalize()}: {result}")