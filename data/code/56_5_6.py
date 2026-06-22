def _validate_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Range bounds must be integers")
    if start < 1 or end < start:
        raise ValueError("Range must start at 1 and end must be at least the start value")
    if end > 100:
        raise ValueError("End value exceeds maximum allowed grid size")
    return True

def generate_multiplication_grid():
    _validate_range(1, 10)
    return [[row * col for col in range(1, 11)] for row in range(1, 11)]

if __name__ == '__main__':
    result = generate_multiplication_grid()
    for row in result:
        print(row)