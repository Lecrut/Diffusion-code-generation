def add(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both arguments must be numbers")
    return a + b

if __name__ == '__main__':
    try:
        print(add(10, 20))
    except ValueError as e:
        print(e)