def _validate_bounds(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Range bounds must be integers")
    if start < 1 or end < 1:
        raise ValueError("Range bounds must be positive")
    if start > end:
        raise ValueError("Start bound cannot exceed end bound")
    return True

def generate_multiplication_grid(start=1, end=10):
    _validate_bounds(start, end)
    return [[r * c for c in range(start, end + 1)] for r in range(start, end + 1)]

if __name__ == '__main__':
    sample_grid = generate_multiplication_grid(1, 10)
    for row in sample_grid:
        print(row)