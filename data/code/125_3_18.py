def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    
    if not (-100 <= a <= 100) or not (-100 <= b <= 100):
        raise ValueError("Inputs must be within the range of -100 to 100.")

def add(a, b):
    validate_numbers(a, b)
    return a + b

def subtract(a, b):
    validate_numbers(a, b)
    return a - b

if __name__ == '__main__':
    print(add(15, 7))
    print(subtract(15, 7))