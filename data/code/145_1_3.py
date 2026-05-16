def test_nested_logic(test_cases):
    results = {}
    for name, logic in test_cases.items():
        expected = logic['expected']
        actual = logic['actual']
        results[name] = {'expected': expected, 'actual': actual}
    return results
if __name__ == '__main__':
    test_data = {
        "simple_and": {
            "expected": False,
            "actual": False
        },
        "simple_or": {
            "expected": True,
            "actual": True
        },
        "nested_and": {
            "expected": False,
            "actual": False
        },
        "nested_or": {
            "expected": True,
            "actual": True
        },
        "complex_logic": {
            "expected": True,
            "actual": True
        }
    }
    results = test_nested_logic(test_data)
    print(results)