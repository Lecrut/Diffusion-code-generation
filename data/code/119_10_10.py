def validate_values(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")

def swap_values(a, b):
    validate_values(a, b)
    a, b = b, a
    return a, b

if __name__ == '__main__':
    x, y = 5, 10
    x, y = swap_values(x, y)
    print(f"x: {x}, y: {y}")