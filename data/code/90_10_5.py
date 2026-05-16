def check_conditions(a, b, c):
    result = (a or b) or c
    return result
if __name__ == '__main__':
    print("--- Test Case 1 ---")
    a1 = False
    b1 = True
    c1 = False
    print(f"Inputs: a={a1}, b={b1}, c={c1}")
    print(f"Result of ({a1} or {b1}) or {c1}: {check_conditions(a1, b1, c1)}")
    print("\n--- Test Case 2 ---")
    a2 = True
    b2 = True
    c2 = True
    print(f"Inputs: a={a2}, b={b2}, c={c2}")
    print(f"Result of ({a2} or {b2}) or {c2}: {check_conditions(a2, b2, c2)}")
    print("\n--- Test Case 3 ---")
    a3 = False
    b3 = False
    c3 = True
    print(f"Inputs: a={a3}, b={b3}, c={c3}")
    print(f"Result of ({a3} or {b3}) or {c3}: {check_conditions(a3, b3, c3)}")
    print("\n--- Test Case 4 ---")
    a4 = True
    b4 = False
    c4 = False
    print(f"Inputs: a={a4}, b={b4}, c={c4}")
    print(f"Result of ({a4} or {b4}) or {c4}: {check_conditions(a4, b4, c4)}")