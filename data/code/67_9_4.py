def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both a and b must be numbers")
    return a + b

if __name__ == '__main__':
    try:
        result = add(10, 20)
        print(result)
    except Exception as e:
        print(e)