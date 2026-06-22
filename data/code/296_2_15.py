def are_in_proportion(a, b, c, d):
    if b == 0 or d == 0:
        raise ValueError("Cannot check proportion when any denominator is zero")
    return a * d == b * c

if __name__ == '__main__':
    x = 3
    y = 4
    u = 6
    v = 8
    print(f"Are {x}, {y}, {u}, {v} in proportion? {are_in_proportion(x, y, u, v)}")