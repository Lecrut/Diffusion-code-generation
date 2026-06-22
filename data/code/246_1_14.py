def add_values(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    return a + b

if __name__ == '__main__':
    print(add_values(3, 5))
    try:
        print(add_values('a', 5))
    except ValueError as e:
        print(e)