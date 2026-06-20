def calculate_difference(num1: float, num2: float) -> float:
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return num1 - num2

if __name__ == '__main__':
    value1 = 150.75
    value2 = 60.25
    result = calculate_difference(value1, value2)
    print(result)