def perform_operations(num1, num2):
    return {
        "addition": num1 + num2,
        "subtraction": num1 - num2,
        "multiplication": num1 * num2,
        "division": num1 / num2 if num2 != 0 else None
    }

if __name__ == '__main__':
    sample_num1 = 10
    sample_num2 = 5
    operation_results = perform_operations(sample_num1, sample_num2)
    print(operation_results)