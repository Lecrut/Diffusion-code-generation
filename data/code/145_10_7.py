if __name__ == '__main__':
    print("--- Testing Nested Boolean Expressions ---")
    a = True
    b = False
    c = True
    test1_result = (a and b) or c
    print(f"Test 1: ({a} and {b}) or {c} -> {test1_result}")
    x = True
    y = False
    z = True
    test2_result = not (x or y) and z
    print(f"Test 2: not ({x} or {y}) and {z} -> {test2_result}")
    p = True
    q = True
    r = False
    s = False
    test3_result = (p or q) and (not r or s)
    print(f"Test 3: ({p} or {q}) and (not {r} or {s}) -> {test3_result}")
    m = False
    n = True
    o = False
    p_val = True
    test4_result = m or (n and (not o or p_val))
    print(f"Test 4: {m} or ({n} and (not {o} or {p_val})) -> {test4_result}")
    a = False
    b = False
    c = False
    test5_result = (a and b) or c
    print(f"Test 5: ({a} and {b}) or {c} -> {test5_result}")
    a = True
    b = True
    c = True
    test6_result = (a and b) or c
    print(f"Test 6: ({a} and {b}) or {c} -> {test6_result}")
    v1 = True
    v2 = False
    v3 = True
    v4 = False
    test7_result = (v1 and not v2) or (v3 and v4)
    print(f"Test 7: ({v1} and not {v2}) or ({v3} and {v4}) -> {test7_result}")