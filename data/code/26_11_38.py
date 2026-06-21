def is_greater(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers")
    return num1 > num2

if __name__ == '__main__':
    sample_value1 = 5.5
    sample_value2 = 3
    try:
        result = is_greater(sample_value1, sample_value2)
        print(result)
    except ValueError as e:
        print(e)