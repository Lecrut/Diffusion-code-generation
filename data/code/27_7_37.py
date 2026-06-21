def check_inequality(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both values must be numeric (int or float).")
    return a != b

if __name__ == '__main__':
    first_value = 100
    second_value = 200.5
    inequality_result = check_inequality(first_value, second_value)
    print(inequality_result)