def validate_input(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numeric.")

def safe_add(a, b):
    validate_input(a, b)
    return a + b

if __name__ == '__main__':
    print(safe_add(5, 10))
    print(safe_add(3.5, 7))
    print(safe_add(-2, 4))