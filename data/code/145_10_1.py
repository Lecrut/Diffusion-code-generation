if __name__ == '__main__':
    print("--- Testing Nested Boolean Expressions ---")
    a = True
    b = False
    c = (a and b) or (not b)
    print(f"Test Case 1 (a={a}, b={b}): Result = {c}")
    x = True
    y = False
    z = (x or y) and (not x or y)
    print(f"Test Case 2 (x={x}, y={y}): Result = {z}")
    p = True
    q = True
    r = False
    s = (p and q) or (r and not p)
    print(f"Test Case 3 (p={p}, q={q}, r={r}): Result = {s}")
    m = True
    n = False
    o = (m ^ n) and (not m)
    print(f"Test Case 4 (m={m}, n={n}): Result = {o}")
    i = True
    j = False
    k = (i or j) and (i and not j)
    print(f"Test Case 5 (i={i}, j={j}): Result = {k}")
    a = False
    b = False
    c = (a and b) or (not b)
    print(f"Test Case 6 (a={a}, b={b}): Result = {c}")
    v1 = True
    v2 = False
    v3 = True
    w = (v1 and v2) or (v3 and not v1)
    print(f"Test Case 7 (v1={v1}, v2={v2}, v3={v3}): Result = {w}")