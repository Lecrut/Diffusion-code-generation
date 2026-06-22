def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a + b

if __name__ == '__main__':
    try:
        result = add(15, 20)
        print(result)
    except ValueError as e:
        print(e)