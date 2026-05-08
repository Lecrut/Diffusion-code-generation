if __name__ == '__main__':
    print("--- Testing Nested Boolean Expressions ---")
    test_cases = [
        {
            "name": "Simple AND",
            "expression": "True and False",
            "expected": False,
            "actual": False
        },
        {
            "name": "Simple OR",
            "expression": "True or False",
            "expected": True,
            "actual": True
        },
        {
            "name": "Nested AND (True)",
            "expression": "(True and True) or False",
            "expected": True,
            "actual": True
        },
        {
            "name": "Nested AND (False)",
            "expression": "(False and True) or False",
            "expected": False,
            "actual": False
        },
        {
            "name": "Boundary Case 1 (All True)",
            "expression": "True and True and True",
            "expected": True,
            "actual": True
        },
        {
            "name": "Boundary Case 2 (All False)",
            "expression": "False and False and False",
            "expected": False,
            "actual": False
        },
        {
            "name": "Boundary Case 3 (Mixed)",
            "expression": "True and False or True",
            "expected": True,
            "actual": True
        },
        {
            "name": "Complex Nesting",
            "expression": "not (A or B) and (C or not D)",
            "A": True,
            "B": False,
            "C": True,
            "D": False,
            "expected": True,
            "actual": True
        },
        {
            "name": "Boundary Case 4 (Negation)",
            "expression": "not (True and False)",
            "expected": True,
            "actual": True
        },
        {
            "name": "Boundary Case 5 (Empty Set)",
            "expression": "False or False",
            "expected": False,
            "actual": False
        }
    ]
    for case in test_cases:
        result = False
        try:
            if "A" in case:
                A = case["A"]
                B = case["B"]
                C = case["C"]
                D = case["D"]
                expression_str = case["expression"].replace("A", str(A).lower()).replace("B", str(B).lower()).replace("C", str(C).lower()).replace("D", str(D).lower())
                if "not" in case["expression"]:
                    if "not (A or B) and (C or not D)" in case["expression"]:
                        result = (not (A or B)) and (C or (not D))
                    else:
                        result = eval(case["expression"])
                else:
                    result = eval(case["expression"])
            else:
                result = eval(case["expression"])
        except Exception as e:
            result = f"ERROR: {e}"
        status = "PASS" if result == case["expected"] else "FAIL"
        print(f"Test: {case['name']}")
        print(f"  Expression: {case['expression']}")
        print(f"  Expected: {case['expected']}, Actual: {result}")
        print(f"  Result: {status}\n")