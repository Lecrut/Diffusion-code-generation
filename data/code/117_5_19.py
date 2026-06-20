def calculate_difference(num1: float, num2: float) -> float:
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return num1 - num2

if __name__ == '__main__':
    try:
        result = calculate_difference(100.5, 45.2)
        print(result)
    except TypeError as e:
        print(e)