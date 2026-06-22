def are_in_proportion(a, b, c, d):
    if b == 0 or d == 0:
        raise ValueError("Denominator in proportion cannot be zero")
    return (a * d) == (b * c)

if __name__ == '__main__':
    a = 10
    b = 2
    c = 5
    d = 1
    print(f"Are {a}, {b}, {c}, and {d} in proportion? {are_in_proportion(a, b, c, d)}")