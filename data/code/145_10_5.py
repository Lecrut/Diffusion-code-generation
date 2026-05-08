def test_nested_boolean_expressions():
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
    result3 = (p and not q) or (r and False)
    print(f"Test Case 3 (p={p}, q={q}, r={r}): Result = {result3}")
    m = False
    n = True
    o = False
    result4 = (m and n) or (not o and False)
    print(f"Test Case 4 (m={m}, n={n}, o={o}): Result = {result4}")
    i = True
    j = True
    k = False
    l = False
    result5 = (i and j) or (not k and l)
    print(f"Test Case 5 (i={i}, j={j}, k={k}, l={l}): Result = {result5}")
    a = False
    b = False
    c = False
    result6 = (a and b) or c
    print(f"Test Case 6 (a={a}, b={b}, c={c}): Result = {result6}")
if __name__ == '__main__':
    test_nested_boolean_expressions()