def check_inequality(value1, value2):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise ValueError("Both values must be numeric (int or float).")
    return value1 != value2

if __name__ == '__main__':
    first_value = 7
    second_value = 3.0
    inequality_result = check_inequality(first_value, second_value)
    print(inequality_result)