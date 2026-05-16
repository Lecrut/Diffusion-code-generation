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
    o = (m or n) and (m and not n)
    print(f"Test Case 4 (m={m}, n={n}): Result = {o}")
    i = True
    j = False
    k = (i and j) or (not i and j)
    print(f"Test Case 5 (i={i}, j={j}): Result = {k}")
    a = False
    b = False
    c = (a or b) and (not a or not b)
    print(f"Test Case 6 (a={a}, b={b}): Result = {c}")
    p = True
    q = False
    r = True
    s = (p and q) or (r and not q)
    print(f"Test Case 7 (p={p}, q={q}, r={r}): Result = {s}")