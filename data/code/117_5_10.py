def calculate_difference(num1: float, num2: float) -> float:
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return num1 - num2

if __name__ == '__main__':
    sample_num1 = 100.5
    sample_num2 = 45.2
    result = calculate_difference(sample_num1, sample_num2)
    print(result)