def add(a, b):
    try:
        return a + b
    except TypeError as e:
        raise ValueError("Both inputs must be numbers") from e

if __name__ == '__main__':
    result = add(4, 6)
    print(result)