def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return a + b

def subtract(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return a - b

if __name__ == '__main__':
    result_add = add(15, 7)
    result_subtract = subtract(15, 7)
    print(f"Sum: {result_add}")
    print(f"Difference: {result_subtract}")