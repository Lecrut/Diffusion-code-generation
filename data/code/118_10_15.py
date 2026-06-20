def multiply(a: float, b: float) -> float:
    if not (isinstance(a, float) and isinstance(b, float)):
        raise ValueError("Both inputs must be floating-point numbers.")
    
    return a * b

if __name__ == '__main__':
    value1 = 3.141592653589793
    value2 = 2.718281828459045
    result = multiply(value1, value2)
    print(result)