def add_decimals(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers")
    return a + b

if __name__ == '__main__':
    try:
        result = add_decimals(3.5, 2.7)
        print(result)
    except ValueError as e:
        print(e)