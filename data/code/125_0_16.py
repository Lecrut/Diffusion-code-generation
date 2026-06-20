def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a + b

def subtract(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a - b

if __name__ == '__main__':
    print(add(15, 27))
    print(subtract(10, 4))