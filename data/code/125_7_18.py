def add(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both inputs must be numbers")
    return a + b

def subtract(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both inputs must be numbers")
    return a - b

if __name__ == '__main__':
    try:
        print(add(5, 3))
        print(subtract(10, 4))
    except ValueError as e:
        print(e)