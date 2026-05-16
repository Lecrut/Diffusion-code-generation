if __name__ == '__main__':
    def test_boolean_expressions():
        print("--- Testing Nested Boolean Expressions ---")
        a = True
        b = False
        c = True
        result1 = (a and b) or (c and not b)
        print(f"Test Case 1 (a=T, b=F, c=T): Result = {result1} (Expected: True)")
        a = False
        b = False
        c = False
        result2 = (a or b) and (not c)
        print(f"Test Case 2 (All False): Result = {result2} (Expected: False)")
        a = True
        b = True
        c = True
        result3 = (a and b) or (c and not b)
        print(f"Test Case 3 (All True): Result = {result3} (Expected: True)")
        a = True
        b = True
        c = False
        result4 = (a and b) or (c and not b)
        print(f"Test Case 4 (a=T, b=T, c=F): Result = {result4} (Expected: True)")
        x = 10
        y = 5
        z = 0
        result5 = (x > 5 and y < 10) or (z == 0 and x != 10)
        print(f"Test Case 5 (x=10, y=5, z=0): Result = {result5} (Expected: True)")
        p = True
        q = False
        r = True
        result6 = not (p or q) and r
        print(f"Test Case 6 (p=T, q=F, r=T): Result = {result6} (Expected: True)")
        m = False
        n = False
        result7 = (m and True) or (not n)
        print(f"Test Case 7 (m=F, n=F): Result = {result7} (Expected: True)")
if __name__ == '__main__':
    test_boolean_expressions()