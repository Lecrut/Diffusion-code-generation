def validate_input(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")

def multiply(a, b):
    validate_input(a, b)
    return a * b

if __name__ == '__main__':
    result = multiply(3.141592653589793, 2.718281828459045)
    print(result)