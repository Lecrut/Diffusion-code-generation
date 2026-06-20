def calculate_difference(num1: float, num2: float) -> float:
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return num1 - num2

if __name__ == '__main__':
    result = calculate_difference(100.5, 45.2)
    print(result)