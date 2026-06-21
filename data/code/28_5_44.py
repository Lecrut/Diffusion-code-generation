def compare_and_report(num1: float, num2: float) -> bool:
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return num1 > num2

if __name__ == '__main__':
    try:
        result = compare_and_report(7.0, 5.5)
        print(result)
    except ValueError as e:
        print(e)