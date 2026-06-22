def add_values(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a + b

if __name__ == '__main__':
    result1 = add_values(3, 5)
    print(result1)
    result2 = add_values(-7, 12)
    print(result2)