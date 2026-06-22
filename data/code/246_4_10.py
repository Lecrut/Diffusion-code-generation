def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return a + b

if __name__ == '__main__':
    x = 10
    y = 25
    result = add_numbers(x, y)
    print(result)