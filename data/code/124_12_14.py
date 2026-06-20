def calculate_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else None
    return {
        "num1": num1,
        "num2": num2,
        "addition": addition,
        "subtraction": subtraction,
        "multiplication": multiplication,
        "division": division
    }

if __name__ == '__main__':
    sample_num1 = 8
    sample_num2 = 4
    operation_result = calculate_operations(sample_num1, sample_num2)
    print(operation_result)