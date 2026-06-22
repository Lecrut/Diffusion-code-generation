def _validate_integers(*values):
    for v in values:
        if not isinstance(v, int) or isinstance(v, bool):
            raise TypeError("All arguments must be integers")

def largest_of_three(a, b, c):
    _validate_integers(a, b, c)
    candidate = a
    if b > candidate:
        candidate = b
    if c > candidate:
        candidate = c
    return candidate

if __name__ == '__main__':
    val_one = 42
    val_two = 17
    val_three = 99
    print(largest_of_three(val_one, val_two, val_three))