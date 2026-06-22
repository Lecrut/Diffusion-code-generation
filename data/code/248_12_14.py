def add(a: int, b: int) -> int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return a + b

if __name__ == '__main__':
    result = add(3, 5)
    print(result)