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
    s = True
    result3 = (p and not q) or (r and s)
    print(f"Test Case 3 (p={p}, q={q}, r={r}, s={s}): Result = {result3}")
    m = False
    n = True
    o = False
    p_val = True
    result4 = m or (n and (not o and p_val))
    print(f"Test Case 4 (m={m}, n={n}, o={o}, p_val={p_val}): Result = {result4}")
    a = False
    b = False
    c = False
    result5 = (a and b) or c
    print(f"Test Case 5 (a={a}, b={b}, c={c}): Result = {result5}")
    a = True
    b = True
    c = True
    result6 = (a and b) or c
    print(f"Test Case 6 (a={a}, b={b}, c={c}): Result = {result6}")
if __name__ == '__main__':
    test_nested_boolean_expressions()