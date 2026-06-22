VALID = "valid"
INVALID = "invalid"

def _validate_size(n):
    if n < 1 or not isinstance(n, int):
        return INVALID
    return VALID

def _build_row(n):
    parts = ["*"] * n
    return "".join(parts)

def render_square(n):
    if _validate_size(n) != VALID:
        return []
    grid = []
    r = 0
    while r < n:
        grid.append(_build_row(n))
        r += 1
    return grid

if __name__ == '__main__':
    SIZE = 9
    square = render_square(SIZE)
    for line in square:
        print(line)