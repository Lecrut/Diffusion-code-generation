def subtract_values(a, b):
    if not (isinstance(a, float) and isinstance(b, float)):
        raise ValueError("Both values must be floats")
    return a - b

if __name__ == '__main__':
    result = subtract_values(10.5, 4.2)
    print(result)