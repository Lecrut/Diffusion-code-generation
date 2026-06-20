def subtract_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    return a - b

if __name__ == '__main__':
    try:
        result = subtract_numbers(10, 5)
        print(result)
    except ValueError as e:
        print(e)