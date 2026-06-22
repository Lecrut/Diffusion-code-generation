def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a + b

if __name__ == '__main__':
    try:
        print(add(15, 25))
    except ValueError as e:
        print(e)