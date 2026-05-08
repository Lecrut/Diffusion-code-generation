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
            "name": "AND with True",
            "expression": "True and True",
            "expected": True,
            "actual": True
        },
        {
            "name": "OR with True",
            "expression": "True or True",
            "expected": True,
            "actual": True
        },
        {
            "name": "AND with False",
            "expression": "True and False",
            "expected": False,
            "actual": False
        },
        {
            "name": "Boundary AND (False)",
            "expression": "False and True",
            "expected": False,
            "actual": False
        },
        {
            "name": "Boundary OR (False)",
            "expression": "False or False",
            "expected": False,
            "actual": False
        },
        {
            "name": "Boundary OR (True)",
            "expression": "True or False",
            "expected": True,
            "actual": True
        },
        {
            "name": "Nested AND",
            "expression": "(True and False) or True",
            "expected": True,
            "actual": True
        },
        {
            "name": "Nested OR",
            "expression": "True or (False and False)",
            "expected": True,
            "actual": True
        },
        {
            "name": "Complex Nested",
            "expression": "not (True and False) or (False or False)",
            "expected": True,
            "actual": True
        },
        {
            "name": "All False",
            "expression": "False and False or False",
            "expected": False,
            "actual": False
        },
        {
            "name": "All True",
            "expression": "True and True or True",
            "expected": True,
            "actual": True
        }
    ]
    for case in test_cases:
        result = eval(case["expression"])
        status = "PASS" if result == case["expected"] else "FAIL"
        print(f"Test: {case['name']}")
        print(f"  Expression: {case['expression']}")
        print(f"  Expected: {case['expected']}, Actual: {case['actual']}")
        print(f"  Result: {status}\n")