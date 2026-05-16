def test_nested_boolean_expressions():
    print("--- Testing Nested Boolean Expressions ---")
    a = True
    b = False
    c = True
    result1 = (a and b) or c
    print(f"Test Case 1 (a={a}, b={b}, c={c}): Result = {result1}")
    x = True
    y = False
    z = True
    result2 = not (x or y) and z
    print(f"Test Case 2 (x={x}, y={y}, z={z}): Result = {result2}")
    p = True
    q = False
    r = True
    result3 = (p or not q) and (r and q)
    print(f"Test Case 3 (p={p}, q={q}, r={r}): Result = {result3}")
    m = False
    n = True
    o = False
    result4 = m or (n and (not o))
    print(f"Test Case 4 (m={m}, n={n}, o={o}): Result = {result4}")
    i = False
    j = False
    k = False
    result5 = (i and j) or (k and not i)
    print(f"Test Case 5 (i={i}, j={j}, k={k}): Result = {result5}")
    s = True
    t = True
    u = True
    result6 = (s and t) or (u and not s)
    print(f"Test Case 6 (s={s}, t={t}, u={u}): Result = {result6}")
if __name__ == '__main__':
    test_nested_boolean_expressions()