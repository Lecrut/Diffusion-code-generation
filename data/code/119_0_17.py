def validate_inputs(a, b):
    if not all(isinstance(i, int) for i in [a, b]):
        raise ValueError("Both inputs must be integers")

def swap(a, b):
    validate_inputs(a, b)
    a, b = b, a
    return a, b

if __name__ == '__main__':
    x, y = 5, 10
    x, y = swap(x, y)
    print(f"x: {x}, y: {y}")