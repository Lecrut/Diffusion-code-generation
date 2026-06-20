def subtract_values(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    return a - b

if __name__ == '__main__':
    result = subtract_values(10, 5)
    print(result)