def _validate_integers(x, y, z):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        raise TypeError("All arguments must be integers")
    return True

def find_largest(a, b, c):
    _validate_integers(a, b, c)
    return max(a, b, c)

if __name__ == '__main__':
    VAL_A = 42
    VAL_B = 99
    VAL_C = 55
    largest_value = find_largest(VAL_A, VAL_B, VAL_C)
    print(largest_value)