def add(a, b):
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise ValueError("Both operands must be numbers")
    return a + b

def subtract(a, b):
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise ValueError("Both operands must be numbers")
    return a - b

if __name__ == '__main__':
    result_add = add(10, 5)
    result_subtract = subtract(10, 5)
    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")