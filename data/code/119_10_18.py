def validate_integers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")

def swap_values(a, b):
    validate_integers(a, b)
    a, b = b, a
    return a, b

if __name__ == '__main__':
    x, y = 5, 10
    x, y = swap_values(x, y)
    print(f"x: {x}, y: {y}")