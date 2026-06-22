def _validate_diagonal(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def calculate_rhombus_area(d1, d2):
    _validate_diagonal(d1, "diagonal1")
    _validate_diagonal(d2, "diagonal2")
    return d1 * d2 * 0.5

if __name__ == '__main__':
    diag_a = 12
    diag_b = 16
    print(calculate_rhombus_area(diag_a, diag_b))