def validate_values(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")

def add_numbers(a, b):
    validate_values(a, b)
    return a + b

if __name__ == '__main__':
    num1 = 42
    num2 = 7
    result = add_numbers(num1, num2)
    print(result)