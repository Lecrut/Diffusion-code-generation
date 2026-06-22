def validate_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")

def add(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    print(f"10 + 5 = {add(10, 5)}")