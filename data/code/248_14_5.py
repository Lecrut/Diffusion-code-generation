def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    return a + b

if __name__ == '__main__':
    result = add_numbers(3, 5)
    print(result)