def add(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers.")
    return a + b

def subtract(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers.")
    return a - b

if __name__ == '__main__':
    print(add(15, 7))
    print(subtract(10, 4))