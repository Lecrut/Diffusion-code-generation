def calculate_difference(num1: float, num2: float) -> float:
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return num1 - num2

if __name__ == '__main__':
    sample_values = {
        "num1": 100,
        "num2": 35
    }
    try:
        result = calculate_difference(sample_values["num1"], sample_values["num2"])
        print(result)
    except TypeError as e:
        print(e)