if __name__ == '__main__':
    print("--- Testing Nested Boolean Expressions ---")
    test_cases = [
        {
            "name": "Simple AND",
            "expression": "True and False",
            "expected": False,
            "actual": (True and False)
        },
        {
            "name": "Simple OR",
            "expression": "True or False",
            "expected": True,
            "actual": (True or False)
        },
        {
            "name": "AND with True",
            "expression": "True and True",
            "expected": True,
            "actual": (True and True)
        },
        {
            "name": "OR with True",
            "expression": "True or True",
            "expected": True,
            "actual": (True or True)
        },
        {
            "name": "AND with False",
            "expression": "True and False",
            "expected": False,
            "actual": (True and False)
        },
        {
            "name": "Boundary AND (False)",
            "expression": "False and True",
            "expected": False,
            "actual": (False and True)
        },
        {
            "name": "Boundary OR (False)",
            "expression": "False or False",
            "expected": False,
            "actual": (False or False)
        },
        {
            "name": "Boundary OR (True)",
            "expression": "True or False",
            "expected": True,
            "actual": (True or False)
        },
        {
            "name": "Nested AND",
            "expression": "(True and False) and True",
            "expected": False,
            "actual": ((True and False) and True)
        },
        {
            "name": "Nested OR",
            "expression": "(True or False) or False",
            "expected": True,
            "actual": ((True or False) or False)
        },
        {
            "name": "Complex Nested",
            "expression": "not (True and False) or (False or False)",
            "expected": True,
            "actual": (not (True and False) or (False or False))
        },
        {
            "name": "All False",
            "expression": "False and False",
            "expected": False,
            "actual": (False and False)
        },
        {
            "name": "All True",
            "expression": "True or True",
            "expected": True,
            "actual": (True or True)
        }
    ]
    for case in test_cases:
        result = case["actual"] == case["expected"]
        status = "PASS" if result else "FAIL"
        print(f"Test: {case['name']}")
        print(f"  Expression: {case['expression']}")
        print(f"  Expected: {case['expected']}")
        print(f"  Actual: {case['actual']}")
        print(f"  Result: {status}\n")