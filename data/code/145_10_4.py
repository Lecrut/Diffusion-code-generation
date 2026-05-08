if __name__ == '__main__':
    print("--- Testing Nested Boolean Expressions ---")
    a = True
    b = False
    c = (a and b) or (not b)
    print(f"Test Case 1 (a=T, b=F): Result = {c}")
    x = True
    y = False
    z = (x or y) and (not x or y)
    print(f"Test Case 2 (x=T, y=F): Result = {z}")
    p = True
    q = True
    r = False
    s = (p and q) or (r and not p)
    print(f"Test Case 3 (p=T, q=T, r=F): Result = {s}")
    m = True
    n = False
    o = (m ^ n) and (not m)
    print(f"Test Case 4 (m=T, n=F): Result = {o}")
    i = False
    j = False
    k = (i or j) and (not i or not j)
    print(f"Test Case 5 (i=F, j=F): Result = {k}")
    p_val = True
    q_val = False
    r_val = True
    t = (p_val and q_val) or (r_val and not q_val)
    print(f"Test Case 6 (p=T, q=F, r=T): Result = {t}")
    a_val = True
    b_val = True
    c_val = True
    d = a_val and b_val or c_val
    print(f"Test Case 7 (a=T, b=T, c=T): Result = {d}")