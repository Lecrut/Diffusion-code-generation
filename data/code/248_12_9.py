def validate_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Both inputs must be numbers")

def add(a: int, b: int) -> int:
    validate_number(a)
    validate_number(b)
    return a + b

if __name__ == '__main__':
    result = add(3, 5)
    print(result)