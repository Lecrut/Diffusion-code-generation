def _validate_numeric(value):
    if not isinstance(value, (int, float)):
        raise TypeError("All arguments must be numeric")

def find_max_value(a, b, c):
    _validate_numeric(a)
    _validate_numeric(b)
    _validate_numeric(c)
    return a if a > b and a > c else (b if b > a and b > c else c)

if __name__ == '__main__':
    val_x = 42.5
    val_y = 99.1
    val_z = 75.3
    output = find_max_value(val_x, val_y, val_z)
    print(output)