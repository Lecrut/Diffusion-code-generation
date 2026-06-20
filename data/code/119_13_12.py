def validate_integers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")

def swap_numbers(x, y):
    validate_integers(x, y)
    return y, x

if __name__ == '__main__':
    a = 15
    b = 25
    swapped_a, swapped_b = swap_numbers(a, b)
    print(f"Swapped values: a={swapped_a}, b={swapped_b}")