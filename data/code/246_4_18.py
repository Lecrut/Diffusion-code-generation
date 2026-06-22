def calculate_sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return a + b

if __name__ == '__main__':
    x = 15
    y = 27
    result = calculate_sum(x, y)
    print(result)