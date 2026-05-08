if __name__ == '__main__':
    print("--- Testing Nested Boolean Expressions ---")
    test_cases = [
        {
            "name": "Simple AND",
            "expression": (True and False) and True,
            "expected": False,
            "result": (True and False) and True
        },
        {
            "name": "Simple OR",
            "expression": (True or False) or False,
            "expected": True,
            "result": (True or False) or False
        },
        {
            "name": "Complex Nesting 1 (Boundary True)",
            "expression": (True and (False or True)) and False,
            "expected": False,
            "result": (True and (False or True)) and False
        },
        {
            "name": "Complex Nesting 2 (Boundary False)",
            "expression": (False and (True or False)) and True,
            "expected": False,
            "result": (False and (True or False)) and True
        },
        {
            "name": "Deep Nesting True",
            "expression": True and (True or (False and True)),
            "expected": True,
            "result": True and (True or (False and True))
        },
        {
            "name": "Deep Nesting False",
            "expression": False and (False or (True and False)),
            "expected": False,
            "result": False and (False or (True and False))
        },
        {
            "name": "Boundary Case 1 (All False)",
            "expression": (False and False) and (False or False),
            "expected": False,
            "result": (False and False) and (False or False)
        },
        {
            "name": "Boundary Case 2 (All True)",
            "expression": (True and True) and (True or True),
            "expected": True,
            "result": (True and True) and (True or True)
        },
        {
            "name": "Mixed Boundary Test",
            "expression": (True or False) and (False and True),
            "expected": False,
            "result": (True or False) and (False and True)
        }
    ]
    all_passed = True
    for case in test_cases:
        actual = case["result"]
        expected = case["expected"]
        status = "PASS" if actual == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"Test: {case['name']}")
        print(f"  Expression: {case['expression']}")
        print(f"  Expected: {expected}")
        print(f"  Actual: {actual}")
        print(f"  Status: {status}\n")
    if all_passed:
        print("--- All tests passed successfully! ---")
    else:
        print("--- Some tests failed! ---")