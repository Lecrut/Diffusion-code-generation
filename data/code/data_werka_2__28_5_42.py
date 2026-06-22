def validate_numbers(num1: float, num2: float) -> None:
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")

def compare_and_report(num1: float, num2: float) -> bool:
    validate_numbers(num1, num2)
    return num1 > num2

if __name__ == '__main__':
    result = compare_and_report(7.0, 5.5)
    print(result)