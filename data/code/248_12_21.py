def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError("Both inputs must be numbers")

if __name__ == '__main__':
    result = add(3, 5)
    print(result)