def evaluate_flags(a, b, c, d):
    return (a and b) or (c and d)

if __name__ == '__main__':
    x = True
    y = False
    p = True
    q = False
    result = evaluate_flags(x, y, p, q)
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"Result of (x and y) or (p and q): {result}")